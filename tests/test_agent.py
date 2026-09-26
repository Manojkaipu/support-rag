"""Agent loop tests against a scripted fake of the Messages API (no network)."""
import asyncio
import copy
import json
from types import SimpleNamespace as NS

import pytest

import rag.agent as agent_mod
from rag.agent import Agent, system_prompt, tools
from rag.llm import AnthropicLLM
from rag.retrieval import Hit


def usage(i=100, o=20):
    return NS(input_tokens=i, output_tokens=o, cache_read_input_tokens=0, cache_creation_input_tokens=0)


def msg(*blocks, stop="tool_use"):
    return NS(stop_reason=stop, content=list(blocks), usage=usage(), model="claude-opus-5")


def text(t):
    return NS(type="text", text=t)


def tool(name, inp, id_):
    return NS(type="tool_use", name=name, input=inp, id=id_)


def verdict(supported, claims=()):
    return msg(text(json.dumps({"supported": supported, "unsupported_claims": list(claims),
                                "feedback": "" if supported else "remove it"})), stop="end_turn")


class FakeClient:
    """Serves agent turns and verifier turns from two scripted queues."""

    def __init__(self, agent_turns, verifier_turns=()):
        self.agent_turns, self.verifier_turns = list(agent_turns), list(verifier_turns)
        self.requests = []
        self.beta = NS(messages=NS(create=self.create))

    async def create(self, **kw):
        self.requests.append(copy.deepcopy(kw))  # the agent keeps mutating its message list
        return (self.agent_turns if "tools" in kw else self.verifier_turns).pop(0)


class FakeRetriever:
    company_id_by_handle = {"Delta": 4, "AppleSupport": 1}

    def __init__(self):
        self.calls = []

    def search(self, query, k, mode, company):
        self.calls.append((query, company))
        return [Hit(317108, 5, 0.03)]

    def describe(self, hits):
        return [{"conversation_id": h.conversation_id, "chunk_id": h.chunk_id, "score": h.score,
                 "company": "Delta", "date": "2017-11-01", "snippet": "Delta: locked for 24 hours"} for h in hits]


def run(agent, q="How long is my Delta account locked?"):
    async def collect():
        return [e async for e in agent.run(q)]
    return asyncio.run(collect())


def fake_llm_for(client_cls_llm, client):
    companies = sorted(FakeRetriever.company_id_by_handle)
    return client_cls_llm(system_prompt(companies), tools(companies), client=client)


@pytest.fixture
def make_agent(monkeypatch):
    def make(client, llm_cls=AnthropicLLM):
        a = Agent(FakeRetriever(), sessionmaker=None, llm=fake_llm_for(llm_cls, client))

        async def fake_get(cid):
            if cid != 317108:
                raise LookupError(f"conversation {cid} doesn't exist")
            return "Conversation #317108 · Delta\nDelta: locked for 24 hours", {"conversation_id": cid}
        monkeypatch.setattr(a, "get_conversation", fake_get)
        return a
    return make


def answer_call(id_, answer="Locked for 24 hours [#317108].", cited=(317108,), answerable=True):
    return tool("submit_answer", {"answer": answer, "cited_conversation_ids": list(cited),
                                  "answerable": answerable}, id_)


def test_happy_path(make_agent):
    client = FakeClient(
        [msg(text("I'll search Delta."), tool("search_conversations", {"query": "account locked", "company": "Delta"}, "t1")),
         msg(answer_call("t2"))],
        [verdict(True)])
    a = make_agent(client)
    events = run(a)
    types = [e.type for e in events]
    assert types == ["text", "tool_call", "tool_result", "tool_call", "verification", "answer", "usage"]
    assert a.retriever.calls == [("account locked", "Delta")]
    ans = events[-2].data
    assert ans["verified"] and ans["cited_conversation_ids"] == [317108]
    usage_ev = events[-1].data
    assert usage_ev["model_calls"] == 3 and usage_ev["cost_usd"] > 0
    # the search result reached the model as a tool_result for the right id
    second = client.requests[1]["messages"]
    assert second[-1]["content"][0]["tool_use_id"] == "t1"
    assert "317108" in second[-1]["content"][0]["content"]
    # every agent request carries the refusal-fallback opt-in and a stable prefix
    agent_reqs = [r for r in client.requests if "tools" in r]
    assert all(r["fallbacks"] == "default" and r["betas"] == AnthropicLLM.BETAS for r in agent_reqs)
    assert agent_reqs[0]["system"] == agent_reqs[1]["system"] and agent_reqs[0]["tools"] == agent_reqs[1]["tools"]


def test_unsupported_answer_is_sent_back_then_revised(make_agent):
    client = FakeClient(
        [msg(answer_call("t1", "Locked 24h and you get a $50 voucher [#317108].")),
         msg(answer_call("t2"))],
        [verdict(False, ["you get a $50 voucher"]), verdict(True)])
    events = run(make_agent(client))
    ver = [e.data for e in events if e.type == "verification"]
    assert [v["supported"] for v in ver] == [False, True]
    feedback = client.requests[2]["messages"][-1]["content"][0]
    assert feedback["is_error"] and "$50 voucher" in feedback["content"]
    assert [e for e in events if e.type == "answer"][0].data["verified"]


def test_gives_up_after_max_retries_and_flags_unverified(make_agent, monkeypatch):
    monkeypatch.setattr(agent_mod.settings, "max_answer_retries", 1)
    client = FakeClient([msg(answer_call("t1")), msg(answer_call("t2"))],
                        [verdict(False, ["x"]), verdict(False, ["x"])])
    events = run(make_agent(client))
    final = [e for e in events if e.type == "answer"][0].data
    assert final["verified"] is False and final["verification"]["unsupported_claims"] == ["x"]


def test_uncited_no_answer_skips_verifier(make_agent):
    client = FakeClient([msg(answer_call("t1", "The history has no Ryanair conversations.", cited=(), answerable=False))])
    events = run(make_agent(client), "Can I bring my dog on Ryanair?")
    final = [e for e in events if e.type == "answer"][0].data
    assert final["answerable"] is False and final["verified"]
    assert not client.verifier_turns and len(client.requests) == 1


def test_tool_errors_are_returned_not_raised(make_agent):
    client = FakeClient([msg(tool("get_conversation", {"conversation_id": 42}, "t1")), msg(answer_call("t2"))],
                        [verdict(True)])
    events = run(make_agent(client))
    err = [e for e in events if e.type == "tool_result"][0].data
    assert "doesn't exist" in err["error"]
    sent = client.requests[1]["messages"][-1]["content"][0]
    assert sent["is_error"] and sent["tool_use_id"] == "t1"


def test_refusal_stops_with_error(make_agent):
    client = FakeClient([msg(text(""), stop="refusal")])
    events = run(make_agent(client))
    assert [e.type for e in events] == ["error", "usage"] and events[0].data["reason"] == "refusal"
