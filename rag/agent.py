"""Question-answering agent over the support corpus.

Loop: the model plans, calls search/get_conversation as often as it needs, then
calls submit_answer. Every submitted answer is checked by a separate verifier
call against the cited conversations; unsupported claims go back to the model
as the submit_answer result and it revises (up to max_answer_retries times).
Nothing reaches the user unverified without being flagged as such.

run() yields Event objects describing each step, which the API streams to the UI.
"""
import asyncio
import json
import time
from dataclasses import asdict, dataclass, field

import anthropic
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from rag.config import PRICES, settings
from rag.db.models import Conversation
from rag.retrieval import Retriever

BETAS = ["server-side-fallback-2026-07-01"]
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
            "strict": True,
            "input_schema": {
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
            "strict": True,
            "input_schema": {
                "type": "object",
                "properties": {"conversation_id": {"type": "integer"}},
                "required": ["conversation_id"],
                "additionalProperties": False,
            },
        },
        {
            "name": "submit_answer",
            "description": "Submit the final answer for verification.",
            "strict": True,
            "input_schema": {
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

VERIFIER_PROMPT = """Check an answer against the support conversations it cites.

A claim is supported only if a company agent in one of the cited conversations said it (or it's a \
fair paraphrase). Claims from the customer, general knowledge, or other companies are unsupported. \
The note that information is from 2017 needs no support. List each unsupported claim; in feedback, \
say briefly how to fix the answer."""


def cost_usd(model: str, usage) -> float:
    p_in, p_out, p_read, p_write = PRICES.get(model, PRICES["claude-opus-5"])
    return ((usage.input_tokens or 0) * p_in + (usage.output_tokens or 0) * p_out
            + (usage.cache_read_input_tokens or 0) * p_read
            + (usage.cache_creation_input_tokens or 0) * p_write) / 1e6


class Agent:
    def __init__(self, retriever: Retriever, sessionmaker, client: anthropic.AsyncAnthropic | None = None):
        self.retriever = retriever
        self.sessionmaker = sessionmaker
        self.client = client or anthropic.AsyncAnthropic()
        self.companies = sorted(retriever.company_id_by_handle)
        self.system = system_prompt(self.companies)
        self.tools = tools(self.companies)

    # ---- tools -------------------------------------------------------------

    async def search(self, query: str, company: str) -> tuple[str, list[dict]]:
        hits = await asyncio.to_thread(self.retriever.search, query, SEARCH_K, "hybrid",
                                       None if company == "any" else company)
        rows = await asyncio.to_thread(self.retriever.describe, hits)
        text = "\n\n".join(f"[#{r['conversation_id']}] {r['company']} · {r['date']}\n{r['snippet'][:SNIPPET_CHARS]}"
                           for r in rows) or "No results."
        return text, rows

    async def get_conversation(self, conversation_id: int) -> tuple[str, dict]:
        async with self.sessionmaker() as s:
            conv = await s.scalar(select(Conversation).where(Conversation.id == conversation_id)
                                  .options(selectinload(Conversation.tweets), selectinload(Conversation.company)))
        if conv is None:
            raise LookupError(f"conversation {conversation_id} doesn't exist")
        lines = [f"Conversation #{conv.id} · {conv.company.handle} · {conv.started_at:%Y-%m-%d}"]
        for t, line in zip(conv.tweets, conv.text.split("\n")):
            lines.append(f"[{t.created_at:%Y-%m-%d %H:%M}] {line}")
        return "\n".join(lines), {"conversation_id": conv.id, "company": conv.company.handle, "turns": conv.n_turns}

    # ---- model calls -------------------------------------------------------

    async def call(self, model, effort, **kwargs):
        return await self.client.beta.messages.create(
            model=model, max_tokens=16000, betas=BETAS, fallbacks="default",
            output_config={"effort": effort, **kwargs.pop("output_config", {})}, **kwargs)

    async def verify(self, question: str, answer: str, cited: list[int]):
        docs = []
        for cid in cited:
            try:
                docs.append((await self.get_conversation(cid))[0])
            except LookupError:
                docs.append(f"Conversation #{cid} doesn't exist.")
        prompt = (f"Question: {question}\n\nAnswer to check:\n{answer}\n\nCited conversations:\n\n"
                  + "\n\n---\n\n".join(docs or ["(none cited)"]))
        resp = await self.call(settings.verifier_model, settings.verifier_effort, system=VERIFIER_PROMPT,
                               messages=[{"role": "user", "content": prompt}],
                               output_config={"format": {"type": "json_schema", "schema": VERDICT_SCHEMA}})
        if resp.stop_reason == "refusal":
            return {"supported": False, "unsupported_claims": [], "feedback": "verifier declined"}, resp
        text = next(b.text for b in resp.content if b.type == "text")
        return json.loads(text), resp

    # ---- loop --------------------------------------------------------------

    async def run(self, question: str):
        messages = [{"role": "user", "content": question}]
        totals = {"input_tokens": 0, "output_tokens": 0, "cache_read_tokens": 0, "cache_write_tokens": 0,
                  "cost_usd": 0.0, "model_calls": 0}
        retries = 0
        t0 = time.perf_counter()

        def account(resp):
            u = resp.usage
            totals["input_tokens"] += u.input_tokens or 0
            totals["output_tokens"] += u.output_tokens or 0
            totals["cache_read_tokens"] += u.cache_read_input_tokens or 0
            totals["cache_write_tokens"] += u.cache_creation_input_tokens or 0
            totals["cost_usd"] += cost_usd(resp.model, u)
            totals["model_calls"] += 1

        for _ in range(settings.max_agent_turns):
            resp = await self.call(settings.agent_model, settings.agent_effort,
                                   system=self.system, tools=self.tools, messages=messages,
                                   thinking={"type": "adaptive", "display": "summarized"},
                                   cache_control={"type": "ephemeral"})
            account(resp)
            if resp.stop_reason in ("refusal", "max_tokens"):
                yield Event("error", {"reason": resp.stop_reason})
                break
            for b in resp.content:
                if b.type == "thinking" and b.thinking:
                    yield Event("thinking", {"text": b.thinking})
                elif b.type == "text" and b.text.strip():
                    yield Event("text", {"text": b.text})
            messages.append({"role": "assistant", "content": resp.content})

            calls = [b for b in resp.content if b.type == "tool_use"]
            if not calls:  # the model stopped without submitting; ask it to submit
                messages.append({"role": "user", "content": "Please call submit_answer with your final answer."})
                continue

            results, final = [], None
            for c in calls:
                yield Event("tool_call", {"id": c.id, "name": c.name, "input": c.input})
            outputs = await asyncio.gather(*(self.execute(c, question) for c in calls), return_exceptions=True)
            for c, out in zip(calls, outputs):
                if isinstance(out, Exception):
                    results.append({"type": "tool_result", "tool_use_id": c.id, "content": f"Error: {out}",
                                    "is_error": True})
                    yield Event("tool_result", {"id": c.id, "name": c.name, "error": str(out)})
                    continue
                text, info, verdict_resp = out
                if verdict_resp is not None:
                    account(verdict_resp)
                if c.name != "submit_answer":
                    results.append({"type": "tool_result", "tool_use_id": c.id, "content": text})
                    yield Event("tool_result", {"id": c.id, "name": c.name, **info})
                    continue
                verdict = info["verdict"]
                yield Event("verification", {"attempt": retries + 1, **verdict})
                if verdict["supported"] or retries >= settings.max_answer_retries:
                    final = {**c.input, "verified": verdict["supported"], "verification": verdict}
                    results.append({"type": "tool_result", "tool_use_id": c.id, "content": "Accepted."})
                else:
                    retries += 1
                    results.append({"type": "tool_result", "tool_use_id": c.id, "is_error": True,
                                    "content": "Verification failed. Unsupported claims: "
                                               + json.dumps(verdict["unsupported_claims"])
                                               + f"\nFeedback: {verdict['feedback']}\nRevise and submit again."})
            messages.append({"role": "user", "content": results})
            if final:
                yield Event("answer", final)
                break
        else:
            yield Event("error", {"reason": "max_turns"})
        yield Event("usage", {**totals, "latency_s": round(time.perf_counter() - t0, 2)})

    async def execute(self, call, question):
        """Returns (tool_result text, event info, verifier response or None)."""
        if call.name == "search_conversations":
            text, rows = await self.search(call.input["query"], call.input["company"])
            return text, {"hits": rows}, None
        if call.name == "get_conversation":
            text, info = await self.get_conversation(call.input["conversation_id"])
            return text, info, None
        if call.name == "submit_answer":
            if not call.input["answerable"] and not call.input["cited_conversation_ids"]:
                verdict = {"supported": True, "unsupported_claims": [], "feedback": "no-answer response"}
                return "", {"verdict": verdict}, None
            verdict, resp = await self.verify(question, call.input["answer"], call.input["cited_conversation_ids"])
            return "", {"verdict": verdict}, resp
        raise ValueError(f"unknown tool {call.name}")
