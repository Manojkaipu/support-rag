"""End-to-end evaluation: run the agent on every eval question, then grade each answer.

Per question it records the agent's answer, citations, verification result, cost,
latency and every conversation retrieved along the way. A judge model then grades:

  grounded     every factual claim is supported by a cited conversation (company agents' words)
  correct      the answer conveys the reference answer's key facts (answerable questions)
  abstained    the answer says the history doesn't cover the question

and assigns one failure mode. One mode comes from the run itself rather than the judge:
retrieval_miss (a failed answerable question whose gold conversations were never
retrieved). The judge's own label is kept as judge_failure_mode.

Results go to results/answers.jsonl and a summary to results/answer_eval.md.

    python eval/answer_eval.py --limit 5        # smoke test
    python eval/answer_eval.py                  # full run
"""
import argparse
import asyncio
import json
from collections import Counter
from pathlib import Path

import anthropic

from rag.agent import Agent, cost_usd
from rag.config import settings
from rag.db.session import make_db
from rag.retrieval import Retriever

EVAL = Path(__file__).parent
OUT = Path("results")

JUDGE_PROMPT = """You grade answers from a question-answering system that may only use a \
customer-support history (Twitter, 2017). You get the question, a reference answer written from \
the source conversation(s), the system's answer, and the conversations the system cited.

Grade:
- grounded: true if every factual claim in the system's answer is stated or fairly paraphrased by a \
company support agent in the cited conversations. A note that information is from 2017 needs no support.
- correct: for answerable questions, true if the answer conveys the reference answer's key facts \
(extra supported detail is fine; missing the main point or contradicting it is not). For unanswerable \
questions, true only if the system declined to answer.
- abstained: true if the system says the history doesn't answer the question.
- failure_mode: "none" if grounded and correct; otherwise the main cause:
    "unsupported_claim"   states something the cited conversations don't support
    "wrong_company"       uses another company's policy or conversations for the one asked about
    "wrong_abstention"    declined although the reference shows the history answers it
    "answered_unanswerable" answered a question the history doesn't cover
    "incomplete"          grounded but misses the reference's main point
    "contradicts_reference" says something the reference contradicts
- rationale: one or two sentences."""

GRADE_SCHEMA = {
    "type": "object",
    "properties": {
        "grounded": {"type": "boolean"},
        "correct": {"type": "boolean"},
        "abstained": {"type": "boolean"},
        "failure_mode": {"type": "string", "enum": ["none", "unsupported_claim", "wrong_company", "wrong_abstention",
                                                    "answered_unanswerable", "incomplete", "contradicts_reference"]},
        "rationale": {"type": "string"},
    },
    "required": ["grounded", "correct", "abstained", "failure_mode", "rationale"],
    "additionalProperties": False,
}


async def run_one(agent: Agent, q: dict) -> dict:
    retrieved, answer, usage, error = [], None, {}, None
    try:
        async for ev in agent.run(q["question"]):
            if ev.type == "tool_result" and "hits" in ev.data:
                retrieved += [h["conversation_id"] for h in ev.data["hits"]]
            elif ev.type == "tool_result" and "conversation_id" in ev.data:
                retrieved.append(ev.data["conversation_id"])
            elif ev.type == "answer":
                answer = ev.data
            elif ev.type == "usage":
                usage = ev.data
            elif ev.type == "error":
                error = ev.data["reason"]
    except anthropic.APIError as e:
        error = f"{type(e).__name__}: {e}"
    return {"id": q["id"], "question": q["question"], "company": q["company"], "type": q["type"],
            "answerable": q["answerable"], "gold": q["gold"], "reference_answer": q["reference_answer"],
            "answer": answer, "retrieved": list(dict.fromkeys(retrieved)), "usage": usage, "error": error}


async def judge(agent: Agent, row: dict) -> tuple[dict, float]:
    a = row["answer"]
    if a is None:
        return {"grounded": False, "correct": False, "abstained": False, "failure_mode": "agent_error",
                "rationale": row["error"] or "no answer"}, 0.0
    docs = []
    for cid in a["cited_conversation_ids"]:
        try:
            docs.append((await agent.get_conversation(cid))[0])
        except LookupError:
            docs.append(f"Conversation #{cid} doesn't exist.")
    prompt = (f"Question: {row['question']}\nAnswerable from the history: {row['answerable']}\n"
              f"Reference answer: {row['reference_answer']}\n\nSystem answer:\n{a['answer']}\n\n"
              "Cited conversations:\n\n" + ("\n\n---\n\n".join(docs) or "(none)"))
    resp = await agent.client.messages.create(
        model=settings.judge_model, max_tokens=4000, system=JUDGE_PROMPT,
        messages=[{"role": "user", "content": prompt}],
        output_config={"effort": "medium", "format": {"type": "json_schema", "schema": GRADE_SCHEMA}})
    if resp.stop_reason == "refusal":
        return {"grounded": False, "correct": False, "abstained": False, "failure_mode": "judge_refused",
                "rationale": ""}, cost_usd(resp.model, resp.usage)
    grade = json.loads(next(b.text for b in resp.content if b.type == "text"))
    # A failed answer whose gold conversation was never retrieved is a retrieval failure first,
    # whatever the answer then did. That's a fact about the run, so it overrides the judge.
    grade["judge_failure_mode"] = grade["failure_mode"]
    if row["answerable"] and grade["failure_mode"] != "none" and not set(row["gold"]) & set(row["retrieved"]):
        grade["failure_mode"] = "retrieval_miss"
    return grade, cost_usd(resp.model, resp.usage)


def summarize(rows: list[dict]) -> str:
    ans = [r for r in rows if r["answerable"]]
    una = [r for r in rows if not r["answerable"]]
    n = len(rows)

    def pct(xs, f):
        return f"{sum(map(f, xs)) / len(xs):.0%} ({sum(map(f, xs))}/{len(xs)})" if xs else "n/a"

    cost = sum(r["usage"].get("cost_usd", 0) for r in rows)
    lat = sorted(r["usage"].get("latency_s", 0) for r in rows if r["usage"])
    lines = [
        "| metric | value |", "|---|---|",
        f"| questions | {n} ({len(ans)} answerable, {len(una)} unanswerable) |",
        f"| correct and grounded (answerable) | {pct(ans, lambda r: r['grade']['correct'] and r['grade']['grounded'])} |",
        f"| grounded (all answers given) | {pct([r for r in rows if r['answer'] and not r['grade']['abstained']], lambda r: r['grade']['grounded'])} |",
        f"| correct abstention (unanswerable) | {pct(una, lambda r: r['grade']['abstained'])} |",
        f"| wrongly abstained (answerable) | {pct(ans, lambda r: r['grade']['abstained'])} |",
        f"| gold conversation retrieved (answerable) | {pct(ans, lambda r: bool(set(r['gold']) & set(r['retrieved'])))} |",
        f"| gold conversation cited (answerable) | {pct(ans, lambda r: bool(r['answer'] and set(r['gold']) & set(r['answer']['cited_conversation_ids'])))} |",
        f"| verifier accepted first draft | {pct([r for r in rows if r['answer']], lambda r: r['answer']['verified'])} |",
        f"| agent cost | ${cost:.2f} total, ${cost / max(n, 1):.3f} per question |",
        f"| judge cost | ${sum(r['judge_cost'] for r in rows):.2f} |",
        f"| latency p50 / p90 | {lat[len(lat) // 2]:.1f}s / {lat[int(len(lat) * 0.9)]:.1f}s |" if lat else "",
        "", "Failure modes:", "", "| mode | count |", "|---|---|",
    ]
    for mode, c in Counter(r["grade"]["failure_mode"] for r in rows).most_common():
        lines.append(f"| {mode} | {c} |")
    return "\n".join(lines) + "\n"


async def main_async(args):
    qs = [json.loads(line) for line in (EVAL / "questions.jsonl").read_text().splitlines()]
    qs = [q for q in qs if q.get("review") != "rejected"][: args.limit or None]
    engine, sessionmaker = make_db()
    agent = Agent(await asyncio.to_thread(Retriever), sessionmaker)
    OUT.mkdir(exist_ok=True)
    path = OUT / "answers.jsonl"
    done = {json.loads(line)["id"] for line in path.read_text().splitlines()} if path.exists() and args.resume else set()
    sem = asyncio.Semaphore(args.concurrency)

    async def one(q):
        async with sem:
            row = await run_one(agent, q)
            row["grade"], row["judge_cost"] = await judge(agent, row)
            print(f"{q['id']} {row['grade']['failure_mode']:22s} ${row['usage'].get('cost_usd', 0):.3f} "
                  f"{row['usage'].get('latency_s', 0):5.1f}s", flush=True)
            return row

    rows = []
    mode = "a" if args.resume else "w"
    with path.open(mode) as f:
        for coro in asyncio.as_completed([one(q) for q in qs if q["id"] not in done]):
            row = await coro
            f.write(json.dumps(row, default=str) + "\n")
            f.flush()
            rows.append(row)
    all_rows = [json.loads(line) for line in path.read_text().splitlines()]
    summary = summarize(sorted(all_rows, key=lambda r: r["id"]))
    (OUT / "answer_eval.md").write_text(summary)
    print(summary)
    await engine.dispose()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--resume", action="store_true", help="skip questions already in results/answers.jsonl")
    asyncio.run(main_async(ap.parse_args()))


if __name__ == "__main__":
    main()
