"""Question-answering agent over the support corpus.

Loop: the model plans, calls search/get_conversation as often as it needs, then
calls submit_answer. Every submitted answer is checked by a separate verifier
call against the cited conversations; unsupported claims go back to the model
as the submit_answer result and it revises (up to max_answer_retries times).
Nothing reaches the user unverified without being flagged as such.

The model provider (Anthropic or xAI) sits behind rag.llm. Tool inputs are
validated here against their schemas, so a malformed call becomes an error
result the model can correct instead of an exception.

run() yields Event objects describing each step, which the API streams to the UI.
"""
import asyncio
import json
import time
from dataclasses import asdict, dataclass, field

from opentelemetry import trace
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from rag.config import settings
from rag.db.models import Conversation
from rag.llm import Turn, make_llm, validate
from rag.observability import TOOL_CALLS, record_llm_call, tracer
from rag.retrieval import Retriever

SEARCH_K = 8
SNIPPET_CHARS = 700


@dataclass
class Event:
    type: str  # thinking | text | tool_call | tool_result | verification | answer | usage | error
    data: dict = field(default_factory=dict)

    def to_dict(self):
        return asdict(self)


def system_prompt(companies: list[str]) -> str:
    return f"""You answer questions using the customer-support history of 108 companies on Twitter \
(about 800,000 conversations, almost all from October-December 2017). You can only rely on what \
company support agents actually said in those conversations.

How to work:
1. Before your first search, write one or two sentences saying what you'll look for.
2. Search with search_conversations. When the question names or clearly implies a company, pass it \
as `company`; otherwise use "any". Rephrase and search again if the first results miss.
3. Open promising conversations with get_conversation before relying on them; search results are \
snippets.
4. Call submit_answer. State what the company's agents said, not general knowledge, and cite every \
conversation you used. If agents gave different answers, say so. Mention that the information is \
from 2017 when it could have changed since.
5. If the history doesn't answer the question, submit with answerable=false and say what is missing. \
Never substitute another company's policy for the one asked about, and don't answer about products \
or services that aren't in the history.

submit_answer is checked against the conversations you cite. If the check finds unsupported \
claims, you'll get them back; fix the answer (search more if needed) and submit again.

Companies (use these exact handles): {", ".join(companies)}"""


def tools(companies: list[str]) -> list[dict]:
    return [
        {
            "name": "search_conversations",
            "description": "Hybrid (BM25 + vector) search over support conversations. Returns up to "
                           f"{SEARCH_K} conversations with the best-matching snippet of each.",
            "schema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "What to look for, in the customer's words."},
                    "company": {"type": "string", "enum": ["any"] + companies,
                                "description": "Company handle to restrict the search to, or 'any'."},
                },
                "required": ["query", "company"],
                "additionalProperties": False,
            },
        },
        {
            "name": "get_conversation",
            "description": "Full text of one conversation, every turn with its timestamp.",
            "schema": {
                "type": "object",
                "properties": {"conversation_id": {"type": "integer"}},
                "required": ["conversation_id"],
                "additionalProperties": False,
            },
        },
        {
            "name": "submit_answer",
            "description": "Submit the final answer for verification.",
            "schema": {
                "type": "object",
                "properties": {
                    "answer": {"type": "string", "description": "Answer for the user, citing conversations as [#id]."},
                    "cited_conversation_ids": {"type": "array", "items": {"type": "integer"}},
                    "answerable": {"type": "boolean",
                                   "description": "False when the history doesn't answer the question."},
                },
                "required": ["answer", "cited_conversation_ids", "answerable"],
                "additionalProperties": False,
            },
        },
    ]


VERDICT_SCHEMA = {
    "type": "object",
    "properties": {
        "supported": {"type": "boolean"},
        "unsupported_claims": {"type": "array", "items": {"type": "string"}},
        "feedback": {"type": "string"},
    },
    "required": ["supported", "unsupported_claims", "feedback"],
    "additionalProperties": False,
}

LAST_TURN = ("You have one turn left. Call submit_answer now: give the best answer the conversations you "
             "have read support, or answerable=false if they don't answer the question.")

VERIFIER_PROMPT = """Check an answer against the support conversations it cites.

A claim is supported only if a company agent in one of the cited conversations said it (or it's a \
fair paraphrase). Claims from the customer, general knowledge, or other companies are unsupported. \
The note that information is from 2017 needs no support. List each unsupported claim; in feedback, \
say briefly how to fix the answer."""


async def load_conversation(sessionmaker, conversation_id: int) -> tuple[str, dict]:
    """A conversation as the agent (and the judges) read it: one line per turn with its timestamp."""
    async with sessionmaker() as s:
        conv = await s.scalar(select(Conversation).where(Conversation.id == conversation_id)
                              .options(selectinload(Conversation.tweets), selectinload(Conversation.company)))
    if conv is None:
        raise LookupError(f"conversation {conversation_id} doesn't exist")
    lines = [f"Conversation #{conv.id} · {conv.company.handle} · {conv.started_at:%Y-%m-%d}"]
    for t, line in zip(conv.tweets, conv.text.split("\n")):
        lines.append(f"[{t.created_at:%Y-%m-%d %H:%M}] {line}")
    return "\n".join(lines), {"conversation_id": conv.id, "company": conv.company.handle, "turns": conv.n_turns}


class Agent:
    def __init__(self, retriever: Retriever, sessionmaker, llm=None):
        self.retriever = retriever
        self.sessionmaker = sessionmaker
        self.companies = sorted(retriever.company_id_by_handle)
        self.system = system_prompt(self.companies)
        self.tools = tools(self.companies)
        self.schemas = {t["name"]: t["schema"] for t in self.tools}
        self.llm = llm or make_llm(self.system, self.tools)

    # ---- tools -------------------------------------------------------------

    async def search(self, query: str, company: str) -> tuple[str, list[dict]]:
        hits = await asyncio.to_thread(self.retriever.search, query, SEARCH_K, "hybrid",
                                       None if company == "any" else company)
        rows = await asyncio.to_thread(self.retriever.describe, hits)
        text = "\n\n".join(f"[#{r['conversation_id']}] {r['company']} · {r['date']}\n{r['snippet'][:SNIPPET_CHARS]}"
                           for r in rows) or "No results."
        return text, rows

    async def get_conversation(self, conversation_id: int) -> tuple[str, dict]:
        return await load_conversation(self.sessionmaker, conversation_id)

    # ---- model calls -------------------------------------------------------

    async def step(self, conv, ctx) -> Turn:
        """One agent turn, traced as llm.agent under the run's root span."""
        with tracer.start_as_current_span("llm.agent", context=ctx) as span:
            span.set_attributes({"gen_ai.request.model": settings.agent_model, "rag.effort": settings.agent_effort})
            t = time.perf_counter()
            turn = await self.llm.step(conv, settings.agent_model, settings.agent_effort)
            span.set_attribute("gen_ai.response.stop_reason", turn.stop_reason)
            record_llm_call("agent", turn.model, turn.usage, turn.cost_usd, time.perf_counter() - t, span)
            return turn

    async def structured(self, role, model, effort, system, prompt, schema):
        """A schema-constrained call (verifier, judge), traced as llm.<role> under the current span.
        Returns (data or None, Turn); data is None when the reply is missing or off-schema."""
        with tracer.start_as_current_span(f"llm.{role}") as span:
            span.set_attributes({"gen_ai.request.model": model, "rag.effort": effort})
            t = time.perf_counter()
            data, turn = await self.llm.structured(model, effort, system, prompt, schema)
            record_llm_call(role, turn.model, turn.usage, turn.cost_usd, time.perf_counter() - t, span)
            if data is not None and validate(data, schema):
                data = None
            return data, turn

    async def verify(self, question: str, answer: str, cited: list[int]):
        docs = []
        for cid in cited:
            try:
                docs.append((await self.get_conversation(cid))[0])
            except LookupError:
                docs.append(f"Conversation #{cid} doesn't exist.")
        prompt = (f"Question: {question}\n\nAnswer to check:\n{answer}\n\nCited conversations:\n\n"
                  + "\n\n---\n\n".join(docs or ["(none cited)"]))
        verdict, turn = await self.structured("verifier", settings.verifier_model, settings.verifier_effort,
                                              VERIFIER_PROMPT, prompt, VERDICT_SCHEMA)
        if verdict is None:
            verdict = {"supported": False, "unsupported_claims": [], "feedback": "the verifier returned no verdict"}
        return verdict, turn

    # ---- loop --------------------------------------------------------------

    async def run(self, question: str):
        # This is an async generator: a span kept "current" across yields would leak into the
        # caller's context, so the root span is passed explicitly to everything below it.
        root = tracer.start_span("agent.run", attributes={"rag.question": question[:500],
                                                          "rag.provider": settings.llm_provider})
        ctx = trace.set_span_in_context(root)
        try:
            async for ev in self._run(question, ctx):
                if ev.type == "answer":
                    root.set_attributes({"rag.answerable": ev.data["answerable"], "rag.verified": ev.data["verified"],
                                         "rag.cited": len(ev.data["cited_conversation_ids"])})
                elif ev.type == "usage":
                    root.set_attributes({"rag.cost_usd": ev.data["cost_usd"], "rag.model_calls": ev.data["model_calls"]})
                elif ev.type == "error":
                    root.set_status(trace.StatusCode.ERROR, ev.data["reason"])
                yield ev
        finally:
            root.end()

    async def _run(self, question: str, ctx):
        conv = self.llm.start(question)
        totals = {"input_tokens": 0, "output_tokens": 0, "cache_read_tokens": 0, "cache_write_tokens": 0,
                  "cost_usd": 0.0, "model_calls": 0}
        retries = 0
        t0 = time.perf_counter()

        def account(turn: Turn):
            u = turn.usage
            totals["input_tokens"] += u.input_tokens
            totals["output_tokens"] += u.output_tokens
            totals["cache_read_tokens"] += u.cache_read_input_tokens
            totals["cache_write_tokens"] += u.cache_creation_input_tokens
            totals["cost_usd"] += turn.cost_usd
            totals["model_calls"] += 1

        for turn_no in range(1, settings.max_agent_turns + 1):
            if turn_no == settings.max_agent_turns and turn_no > 1:
                self.llm.add_user_text(conv, LAST_TURN)  # end with an answer or an abstention, not a timeout
            turn = await self.step(conv, ctx)
            account(turn)
            if turn.stop_reason in ("refusal", "max_tokens"):
                yield Event("error", {"reason": turn.stop_reason})
                break
            for text in turn.thinking:
                yield Event("thinking", {"text": text})
            for text in turn.text:
                yield Event("text", {"text": text})

            calls = turn.tool_calls
            if not calls:  # the model stopped without submitting; ask it to submit
                self.llm.add_user_text(conv, "Please call submit_answer with your final answer.")
                continue

            results, final = [], None
            for c in calls:
                yield Event("tool_call", {"id": c.id, "name": c.name,
                                          "input": c.input if c.input is not None else {"raw": c.raw}})
            outputs = await asyncio.gather(*(self.execute(c, question, ctx) for c in calls), return_exceptions=True)
            for c, out in zip(calls, outputs):
                if isinstance(out, Exception):
                    results.append((c.id, f"Error: {out}", True))
                    yield Event("tool_result", {"id": c.id, "name": c.name, "error": str(out)})
                    continue
                text, info, verdict_turn = out
                if verdict_turn is not None:
                    account(verdict_turn)
                if c.name != "submit_answer":
                    results.append((c.id, text, False))
                    yield Event("tool_result", {"id": c.id, "name": c.name, **info})
                    continue
                verdict = info["verdict"]
                yield Event("verification", {"attempt": retries + 1, **verdict})
                last_turn = turn_no == settings.max_agent_turns  # no turn left to revise: show it, flagged
                if verdict["supported"] or retries >= settings.max_answer_retries or last_turn:
                    final = {**c.input, "verified": verdict["supported"], "verification": verdict}
                    results.append((c.id, "Accepted.", False))
                else:
                    retries += 1
                    results.append((c.id, "Verification failed. Unsupported claims: "
                                    + json.dumps(verdict["unsupported_claims"])
                                    + f"\nFeedback: {verdict['feedback']}\nRevise and submit again.", True))
            self.llm.add_tool_results(conv, results)
            if final:
                yield Event("answer", final)
                break
        else:
            yield Event("error", {"reason": "max_turns"})
        yield Event("usage", {**totals, "latency_s": round(time.perf_counter() - t0, 2)})

    async def execute(self, call, question, ctx=None):
        """Runs one tool call in a tool.<name> span. Returns (tool_result text, event info,
        verifier Turn or None). Raises on bad input; the loop turns that into an error result."""
        with tracer.start_as_current_span(f"tool.{call.name}", context=ctx) as span:
            span.set_attribute("rag.tool_input", (json.dumps(call.input) if call.input is not None else call.raw)[:500])
            try:
                out = await self._execute(call, question)
            except Exception as e:
                TOOL_CALLS.labels(call.name, "error").inc()
                span.record_exception(e)
                span.set_status(trace.StatusCode.ERROR, str(e))
                raise
            TOOL_CALLS.labels(call.name, "ok").inc()
            return out

    async def _execute(self, call, question):
        schema = self.schemas.get(call.name)
        if schema is None:
            raise ValueError(f"unknown tool {call.name}")
        if call.input is None:
            raise ValueError("the arguments were not valid JSON")
        errors = validate(call.input, schema)
        if errors:
            raise ValueError("invalid arguments: " + "; ".join(errors))
        if call.name == "search_conversations":
            text, rows = await self.search(call.input["query"], call.input["company"])
            return text, {"hits": rows}, None
        if call.name == "get_conversation":
            text, info = await self.get_conversation(call.input["conversation_id"])
            return text, info, None
        # submit_answer
        if not call.input["answerable"] and not call.input["cited_conversation_ids"]:
            verdict = {"supported": True, "unsupported_claims": [], "feedback": "no-answer response"}
            return "", {"verdict": verdict}, None
        verdict, turn = await self.verify(question, call.input["answer"], call.input["cited_conversation_ids"])
        return "", {"verdict": verdict}, turn
