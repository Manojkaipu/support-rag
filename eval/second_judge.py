"""Re-grades every answer in results/answers.jsonl with an independent judge from a
different model family (OpenAI; the agent and first judge are Grok), using the same
rubric and the same conversation text, then measures how often the two agree.

Writes results/judge2.jsonl, results/judge_agreement.md, and eval/grading_sheet.md +
eval/human_grades.jsonl: 10 answers for hand grading, disagreements first.

    python -m eval.second_judge            # grade (resumable) + agreement + hand-grading sample
    python -m eval.second_judge --report   # agreement + sample only, no API calls
"""
import argparse
import asyncio
import json
import random
from pathlib import Path

from eval.answer_eval import GRADE_SCHEMA, JUDGE_PROMPT, judge_prompt
from eval.judge_agreement import DIMS, kappa, write_items
from rag.agent import load_conversation
from rag.config import settings
from rag.db.session import make_db
from rag.llm import OpenAILLM, validate

OUT = Path("results")
ANSWERS, JUDGE2 = OUT / "answers.jsonl", OUT / "judge2.jsonl"


async def grade_all(concurrency: int):
    rows = [json.loads(line) for line in ANSWERS.read_text().splitlines()]
    done = {json.loads(line)["id"] for line in JUDGE2.read_text().splitlines()} if JUDGE2.exists() else set()
    import openai

    engine, sessionmaker = make_db()
    llm = OpenAILLM("", [], client=openai.AsyncOpenAI(api_key=settings.openai_api_key, max_retries=8))
    sem = asyncio.Semaphore(concurrency)

    async def one(row):
        async with sem:
            if row["answer"] is None:
                return {"id": row["id"], "grade": None, "cost_usd": 0.0}
            prompt = await judge_prompt(lambda cid: load_conversation(sessionmaker, cid), row)
            for attempt in range(6):  # new accounts have low tokens-per-minute limits
                try:
                    data, turn = await llm.structured(settings.second_judge_model, "medium", JUDGE_PROMPT,
                                                      prompt, GRADE_SCHEMA)
                    break
                except openai.RateLimitError:
                    if attempt == 5:
                        raise
                    await asyncio.sleep(15 * (attempt + 1))
            if data is not None and validate(data, GRADE_SCHEMA):
                data = None
            print(f"{row['id']} {'ok' if data else 'NO GRADE'} ${turn.cost_usd:.4f}", flush=True)
            return {"id": row["id"], "grade": data, "cost_usd": turn.cost_usd, "model": turn.model}

    with JUDGE2.open("a") as f:
        for coro in asyncio.as_completed([one(r) for r in rows if r["id"] not in done]):
            f.write(json.dumps(await coro) + "\n")
            f.flush()
    await engine.dispose()


def report(n_human: int = 10, seed: int = 0):
    rows = {r["id"]: r for r in map(json.loads, ANSWERS.read_text().splitlines())}
    j2 = {r["id"]: r for r in map(json.loads, JUDGE2.read_text().splitlines())}
    both = [i for i in rows if rows[i]["answer"] and j2.get(i, {}).get("grade")]
    lines = [f"Grok judge ({settings.judge_model}) vs independent judge ({settings.second_judge_model}), "
             f"same rubric, {len(both)} answers.", "",
             "| dimension | agreement | Cohen's kappa | first judge true | second judge true |", "|---|---|---|---|---|"]
    disagree = {}
    for d in DIMS:
        a = [bool(rows[i]["grade"][d]) for i in both]
        b = [bool(j2[i]["grade"][d]) for i in both]
        lines.append(f"| {d} | {sum(x == y for x, y in zip(a, b)) / len(a):.0%} | {kappa(a, b):.2f} "
                     f"| {sum(a)} | {sum(b)} |")
        for i, x, y in zip(both, a, b):
            if x != y:
                disagree.setdefault(i, []).append(d)
    j1_pass = sum(rows[i]["grade"]["grounded"] and rows[i]["grade"]["correct"] for i in both)
    j2_pass = sum(j2[i]["grade"]["grounded"] and j2[i]["grade"]["correct"] for i in both)
    cost = sum(r["cost_usd"] for r in j2.values())
    lines += ["", f"Grounded and correct: first judge {j1_pass}/{len(both)}, second judge {j2_pass}/{len(both)}. "
              f"Second-judge cost ${cost:.2f}.", "", f"Disagreements ({len(disagree)}):", ""]
    for i, dims in sorted(disagree.items()):
        lines.append(f"- {i} on {', '.join(dims)}: first judge: {rows[i]['grade']['rationale']} "
                     f"| second judge: {j2[i]['grade']['rationale']}")
    (OUT / "judge_agreement.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))

    # Hand-grading sample: every disagreement first (up to n), then random agreed answers.
    rng = random.Random(seed)
    picked = sorted(disagree)[:n_human]
    rest = [i for i in both if i not in disagree]
    picked += rng.sample(rest, min(len(rest), n_human - len(picked)))
    rng.shuffle(picked)
    write_items([rows[i] for i in picked])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="skip grading, only report")
    ap.add_argument("--concurrency", type=int, default=2)
    ap.add_argument("--n-human", type=int, default=10)
    a = ap.parse_args()
    if not a.report:
        asyncio.run(grade_all(a.concurrency))
    report(a.n_human)


if __name__ == "__main__":
    main()
