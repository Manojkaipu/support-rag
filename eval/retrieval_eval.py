"""Retrieval quality on the answerable eval questions: vector vs BM25 vs hybrid,
with and without the question's company as a filter.

Metrics are per question, at conversation level:
  hit@k   - at least one gold conversation in the top k
  recall@k - fraction of the question's gold conversations in the top k
  MRR     - 1 / rank of the first gold conversation (0 if not in top 50)

Gold labels list the conversations the question was written from. Other
conversations can answer the same question, so these numbers are lower bounds.
Latency includes embedding the query (MiniLM on CPU).

    python eval/retrieval_eval.py
"""
import json
import time
from pathlib import Path

import numpy as np
import pandas as pd

from rag.retrieval import MODES, Retriever

EVAL = Path(__file__).parent
KS = (1, 5, 10, 20)


def main():
    qs = [json.loads(line) for line in (EVAL / "questions.jsonl").read_text().splitlines()]
    qs = [q for q in qs if q["answerable"] and q.get("review") != "rejected"]
    r = Retriever()
    for q in qs[:10]:  # warm-up: model, caches, page faults on the index
        for mode in MODES:
            r.search(q["question"], k=50, mode=mode)
    rows, per_q = [], []
    for filtered in (False, True):
        for mode in MODES:
            stats = {f"hit@{k}": [] for k in KS} | {f"recall@{k}": [] for k in KS} | {"mrr": [], "ms": []}
            for q in qs:
                t = time.perf_counter()
                hits = r.search(q["question"], k=50, mode=mode, company=q["company"] if filtered else None)
                stats["ms"].append((time.perf_counter() - t) * 1e3)
                ranked = [h.conversation_id for h in hits]
                gold = set(q["gold"])
                first = next((i + 1 for i, c in enumerate(ranked) if c in gold), None)
                stats["mrr"].append(1.0 / first if first else 0.0)
                for k in KS:
                    found = gold & set(ranked[:k])
                    stats[f"hit@{k}"].append(float(bool(found)))
                    stats[f"recall@{k}"].append(len(found) / len(gold))
                per_q.append({"id": q["id"], "type": q["type"], "mode": mode, "filtered": filtered,
                              "first_gold_rank": first})
            ms = stats.pop("ms")
            row = {"mode": mode, "company_filter": filtered} | {k: float(np.mean(v)) for k, v in stats.items()}
            row["p50_ms"] = float(np.median(ms))
            rows.append(row)
            print(f"{mode:7s} filter={filtered!s:5s}  " + "  ".join(
                f"{k}={row[k]:.3f}" for k in ("hit@1", "hit@5", "hit@10", "recall@10", "mrr")) +
                  f"  p50={row['p50_ms']:.1f}ms", flush=True)

    out = Path("results")
    out.mkdir(exist_ok=True)
    pd.DataFrame(rows).to_csv(out / "retrieval.csv", index=False)
    pd.DataFrame(per_q).to_csv(out / "retrieval_per_question.csv", index=False)
    print(f"wrote {out / 'retrieval.csv'} ({len(qs)} questions)")


if __name__ == "__main__":
    main()
