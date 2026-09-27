"""Checks the LLM judge against human grades.

1. `python eval/judge_agreement.py sample` picks 20 graded answers (stratified so
   failures are represented) and writes eval/human_grades.jsonl with the judge's
   labels hidden. Fill in grounded / correct / abstained for each by hand.
2. `python eval/judge_agreement.py score` compares your labels with the judge's:
   raw agreement and Cohen's kappa per dimension, plus every disagreement.
"""
import json
import random
import sys
from pathlib import Path

EVAL = Path(__file__).parent
ANSWERS = Path("results/answers.jsonl")
HUMAN = EVAL / "human_grades.jsonl"
SHEET = EVAL / "grading_sheet.md"
DIMS = ("grounded", "correct", "abstained")


def sample(n=20, seed=0):
    rows = [json.loads(line) for line in ANSWERS.read_text().splitlines()]
    rows = [r for r in rows if r["answer"]]
    fails = [r for r in rows if r["grade"]["failure_mode"] != "none"]
    passes = [r for r in rows if r["grade"]["failure_mode"] == "none"]
    rng = random.Random(seed)
    k = min(len(fails), n // 2)
    picked = rng.sample(fails, k) + rng.sample(passes, min(len(passes), n - k))
    rng.shuffle(picked)
    with HUMAN.open("w") as f:
        for r in picked:
            f.write(json.dumps({"id": r["id"], "question": r["question"], "reference_answer": r["reference_answer"],
                                "answer": r["answer"]["answer"], "cited": r["answer"]["cited_conversation_ids"],
                                "grounded": None, "correct": None, "abstained": None, "notes": ""},
                               ensure_ascii=False) + "\n")
    write_sheet(picked)
    print(f"wrote {len(picked)} items to {HUMAN} and a reading copy to {SHEET}")


def write_sheet(picked):
    """Markdown copy of the items with the cited conversations inlined, for reading while grading."""
    import pandas as pd

    conv = pd.read_parquet("data/conversations.parquet", columns=["id", "text"]).set_index("id")["text"]
    out = ["# Hand grading", "",
           "For each answer, judge only from the cited conversations (and the reference answer):",
           "- **grounded**: every factual claim is said (or fairly paraphrased) by a company agent in a cited conversation",
           "- **correct**: it conveys the reference answer's main point (for unanswerable questions: it declined)",
           "- **abstained**: it says the history doesn't answer the question",
           "",
           "Record true/false for each in eval/human_grades.jsonl (the item with the same id), plus notes.", ""]
    for r in picked:
        a = r["answer"]
        out += [f"## {r['id']}", "", f"**Question:** {r['question']}", "",
                f"**Reference:** {r['reference_answer']}", "", "**System answer:**", "", a["answer"], ""]
        for cid in a["cited_conversation_ids"]:
            out += [f"<details><summary>cited conversation #{cid}</summary>", "", "```",
                    conv.get(cid, "(missing)"), "```", "</details>", ""]
        if not a["cited_conversation_ids"]:
            out += ["_(no conversations cited)_", ""]
    SHEET.write_text("\n".join(out))


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return float("nan") if pe == 1 else (po - pe) / (1 - pe)


def score():
    human = [json.loads(line) for line in HUMAN.read_text().splitlines()]
    human = [h for h in human if all(h[d] is not None for d in DIMS)]
    judge = {r["id"]: r["grade"] for r in map(json.loads, ANSWERS.read_text().splitlines())}
    print(f"{len(human)} hand-graded answers\n")
    print("| dimension | agreement | Cohen's kappa |\n|---|---|---|")
    for d in DIMS:
        h = [bool(x[d]) for x in human]
        j = [bool(judge[x["id"]][d]) for x in human]
        agree = sum(x == y for x, y in zip(h, j)) / len(h)
        print(f"| {d} | {agree:.0%} | {kappa(h, j):.2f} |")
    print("\nDisagreements:")
    for x in human:
        diff = [d for d in DIMS if bool(x[d]) != bool(judge[x["id"]][d])]
        if diff:
            print(f"- {x['id']} {diff}: judge said {judge[x['id']]['rationale']!r}; notes: {x['notes']!r}")


if __name__ == "__main__":
    {"sample": sample, "score": score}[sys.argv[1]]()
