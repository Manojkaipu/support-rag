"""Validates eval/questions_draft.jsonl and writes eval/questions.jsonl plus a
review sheet (eval/review_sheet.md) showing each question next to its gold
conversations.

Gold labels are stored as root tweet ids too, so they survive a re-ingest that
renumbers conversations.

    python eval/build_questions.py
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

import vecsearch as vs

EVAL = Path(__file__).parent
DATA = Path("data")


def main():
    qs = [json.loads(line) for line in (EVAL / "questions_draft.jsonl").read_text().splitlines() if line.strip()]
    conv = pd.read_parquet(DATA / "conversations.parquet", columns=["id", "root_tweet_id", "company_id", "text"])
    companies = pd.read_parquet(DATA / "companies.parquet")
    handle = dict(zip(companies.id, companies.handle))
    conv = conv.set_index("id")

    errors = []
    ids = [q["id"] for q in qs]
    if len(set(ids)) != len(ids):
        errors.append("duplicate question ids")
    for q in qs:
        if q["answerable"] and not q["gold"]:
            errors.append(f"{q['id']}: answerable but no gold conversation")
        if not q["answerable"] and q["gold"]:
            errors.append(f"{q['id']}: unanswerable but has gold")
        for g in q["gold"]:
            if g not in conv.index:
                errors.append(f"{q['id']}: gold conversation {g} doesn't exist")
            elif handle[conv.at[g, "company_id"]] != q["company"]:
                errors.append(f"{q['id']}: gold {g} is {handle[conv.at[g, 'company_id']]}, question says {q['company']}")
    if errors:
        raise SystemExit("\n".join(errors))

    bm25 = vs.BM25Index.load(str(DATA / "bm25.bin"))
    chunk_conv = np.load(DATA / "chunk_conversation.npy")
    out, sheet = [], ["# Evaluation set review", "",
                      "For each question: check that the question is natural, the reference answer only says what the "
                      "company said, and the gold conversations really answer it. Set `review` in questions.jsonl to "
                      "`approved`, `edited` (after fixing it) or `rejected`.", ""]
    for q in qs:
        q = dict(q)
        q["gold_root_tweet_ids"] = [int(conv.at[g, "root_tweet_id"]) for g in q["gold"]]
        q.setdefault("review", "pending")
        out.append(q)
        sheet += [f"## {q['id']} · {q['company'] or 'no company'} · {q['type']}", "",
                  f"**Q:** {q['question']}", "", f"**Reference:** {q['reference_answer']}", ""]
        for g in q["gold"]:
            sheet += [f"<details><summary>gold conversation {g}</summary>", "", "```",
                      conv.at[g, "text"], "```", "</details>", ""]
        if not q["answerable"]:
            ids_, scores = bm25.search(q["question"], k=5)
            sheet += ["Top BM25 hits (confirm none of them answers the question):", ""]
            for i, s in zip(ids_[0], scores[0]):
                if i < 0:
                    continue
                c = int(chunk_conv[i])
                first = conv.at[c, "text"].split("\n")[:2]
                sheet.append(f"- {s:.1f} [{handle[conv.at[c, 'company_id']]}] conv {c}: "
                             + " / ".join(t[:120] for t in first))
            sheet.append("")

    (EVAL / "questions.jsonl").write_text("".join(json.dumps(q, ensure_ascii=False) + "\n" for q in out))
    (EVAL / "review_sheet.md").write_text("\n".join(sheet))
    n_ans = sum(q["answerable"] for q in out)
    print(f"{len(out)} questions ({n_ans} answerable, {len(out) - n_ans} unanswerable), "
          f"{sum(len(q['gold']) for q in out)} gold conversations, "
          f"{len({q['company'] for q in out if q['company']})} companies")


if __name__ == "__main__":
    main()
