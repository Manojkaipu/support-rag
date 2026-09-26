"""xAI backend (Responses API) against a scripted fake client, plus schema validation."""
import copy
import json
from types import SimpleNamespace as NS

from rag.llm import XaiLLM, validate
from tests.test_agent import run

TICKS = 37_756_000  # $0.0037756 per call


def usage(inp=1000, cached=600, out=200):
    return NS(input_tokens=inp, output_tokens=out, input_tokens_details=NS(cached_tokens=cached),
              output_tokens_details=NS(reasoning_tokens=150), cost_in_usd_ticks=TICKS)


def resp(id_, *items, status="completed"):
    return NS(id=id_, status=status, model="grok-4.7", output=list(items), usage=usage())


def message(text):
    return NS(type="message", content=[NS(type="output_text", text=text)])


def call(call_id, name, args):
    return NS(type="function_call", call_id=call_id, name=name,
              arguments=args if isinstance(args, str) else json.dumps(args))


def verdict(supported, claims=()):
    return resp("v", message(json.dumps({"supported": supported, "unsupported_claims": list(claims),
                                         "feedback": "" if supported else "fix it"})))


def submit(call_id, cited=(317108,)):
    return call(call_id, "submit_answer", {"answer": "Locked for 24 hours [#317108].",
                                           "cited_conversation_ids": list(cited), "answerable": True})


class FakeXai:
    def __init__(self, agent_turns, structured_turns=()):
        self.agent_turns, self.structured_turns = list(agent_turns), list(structured_turns)
        self.requests = []
        self.responses = NS(create=self.create)

    async def create(self, **kw):
        self.requests.append(copy.deepcopy(kw))
        return (self.structured_turns if "text" in kw else self.agent_turns).pop(0)


def test_xai_happy_path_chains_responses(make_agent):
    client = FakeXai([resp("r1", message("Searching Delta."), call("c1", "search_conversations",
                                                                   {"query": "locked", "company": "Delta"})),
                      resp("r2", submit("c2"))],
                     [verdict(True)])
    events = run(make_agent(client, XaiLLM))
    assert [e.type for e in events] == ["text", "tool_call", "tool_result", "tool_call", "verification",
                                        "answer", "usage"]
    first, second = [r for r in client.requests if "tools" in r]
    assert [m["role"] for m in first["input"]] == ["system", "user"] and first["previous_response_id"] is None
    assert second["previous_response_id"] == "r1"
    assert second["input"] == [{"type": "function_call_output", "call_id": "c1",
                                "output": second["input"][0]["output"]}]
    assert "317108" in second["input"][0]["output"]
    assert all(t["type"] == "function" and "parameters" in t for t in first["tools"])
    u = events[-1].data
    assert u["model_calls"] == 3 and abs(u["cost_usd"] - 3 * TICKS / 1e10) < 1e-12
    assert u["input_tokens"] == 3 * 400 and u["cache_read_tokens"] == 3 * 600


def test_xai_verifier_request_uses_json_schema(make_agent):
    client = FakeXai([resp("r1", submit("c1"))], [verdict(True)])
    run(make_agent(client, XaiLLM))
    v = next(r for r in client.requests if "text" in r)
    fmt = v["text"]["format"]
    assert fmt["type"] == "json_schema" and fmt["strict"] is True
    assert set(fmt["schema"]["required"]) == {"supported", "unsupported_claims", "feedback"}
    assert v["store"] is False


def test_xai_bad_arguments_become_fixable_errors(make_agent):
    client = FakeXai([resp("r1", call("c1", "get_conversation", "{not json"),
                           call("c2", "search_conversations", {"query": "x", "company": "NoSuchCo"})),
                      resp("r2", submit("c3"))],
                     [verdict(True)])
    events = run(make_agent(client, XaiLLM))
    errors = [e.data["error"] for e in events if e.type == "tool_result"]
    assert "not valid JSON" in errors[0] and "company must be one of the allowed values" in errors[1]
    sent = client.requests[1]["input"]
    assert [i["call_id"] for i in sent] == ["c1", "c2"] and all(i["output"].startswith("Error:") for i in sent)
    assert [e for e in events if e.type == "answer"][0].data["verified"]


def test_xai_unsupported_answer_is_revised(make_agent):
    client = FakeXai([resp("r1", submit("c1")), resp("r2", submit("c2"))],
                     [verdict(False, ["a $50 voucher"]), verdict(True)])
    events = run(make_agent(client, XaiLLM))
    assert [e.data["supported"] for e in events if e.type == "verification"] == [False, True]
    feedback = client.requests[2]["input"][0]
    assert feedback["call_id"] == "c1" and "$50 voucher" in feedback["output"]


def test_xai_off_schema_verdict_is_not_trusted(make_agent):
    bad = resp("v", message(json.dumps({"supported": "yes"})))  # wrong type, missing fields
    client = FakeXai([resp("r1", submit("c1")), resp("r2", submit("c2")), resp("r3", submit("c3"))],
                     [bad, bad, bad])
    events = run(make_agent(client, XaiLLM))
    final = [e for e in events if e.type == "answer"][0].data
    assert final["verified"] is False and final["verification"]["feedback"] == "the verifier returned no verdict"


def test_last_turn_is_told_to_submit(make_agent, monkeypatch):
    import rag.agent as agent_mod

    monkeypatch.setattr(agent_mod.settings, "max_agent_turns", 3)
    search = lambda cid: call(cid, "search_conversations", {"query": "q", "company": "any"})  # noqa: E731
    client = FakeXai([resp("r1", search("c1")), resp("r2", search("c2")), resp("r3", submit("c3"))],
                     [verdict(True)])
    events = run(make_agent(client, XaiLLM))
    agent_reqs = [r for r in client.requests if "tools" in r]
    assert not any(i.get("content") == agent_mod.LAST_TURN for r in agent_reqs[:2] for i in r["input"])
    assert agent_reqs[2]["input"][-1] == {"role": "user", "content": agent_mod.LAST_TURN}
    assert [e for e in events if e.type == "answer"][0].data["verified"]


def test_xai_incomplete_response_stops(make_agent):
    client = FakeXai([resp("r1", message("partial"), status="incomplete")])
    events = run(make_agent(client, XaiLLM))
    assert [e.type for e in events] == ["error", "usage"] and events[0].data["reason"] == "max_tokens"


def test_validate():
    schema = {"type": "object", "additionalProperties": False, "required": ["a", "b"],
              "properties": {"a": {"type": "integer"}, "b": {"type": "array", "items": {"type": "string"}},
                             "c": {"type": "string", "enum": ["x", "y"]}}}
    assert validate({"a": 1, "b": ["s"], "c": "x"}, schema) == []
    errs = validate({"a": True, "b": [1], "c": "z", "d": 0}, schema)
    assert errs == ["input.d is not allowed", "input.a must be an integer", "input.b[0] must be a string",
                    "input.c must be one of the allowed values"]
    assert validate({}, schema) == ["input.a is required", "input.b is required"]
