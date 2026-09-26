"""Filtered vector search on the real chunk index: recall and latency by filter selectivity.

Strategies, for companies from ~9% of chunks down to ~0.01%:
  post      - unfiltered HNSW search for k * overfetch, then drop other companies (naive baseline)
  in-graph  - vecsearch filter during the graph walk (exact_below=0)
  exact     - scan only the allowed chunks
Recall@10 is against exact filtered top-10. One query thread, idle machine.

    python bench/filter_bench.py
"""
import time
from pathlib import Path

import numpy as np
import pandas as pd

import vecsearch as vs
from rag.config import settings

K, EF, OVERFETCH = 10, 128, 10
COMPANIES = ["AmazonHelp", "Uber_Support", "Delta", "VirginTrains", "McDonalds", "DropboxSupport",
             "TfL", "AskRobinhood", "CarlsJr", "HotelTonightCX"]


def timed(fn, queries):
    out, lat = [], []
    for q in queries:
        t = time.perf_counter()
        out.append(fn(q[None, :]))
        lat.append((time.perf_counter() - t) * 1e3)
    return out, np.array(lat)


def main():
    d = settings.data_dir
    idx = vs.HNSWIndex.load(str(d / "hnsw.bin"))
    n = len(idx)
    x = np.fromfile(d / "chunk_emb.f32", dtype=np.float32).reshape(n, -1)
    company = np.load(d / "chunk_company.npy")
    handles = pd.read_parquet(d / "companies.parquet").set_index("handle")["id"]

    rng = np.random.default_rng(0)
    rows = []
    for name in COMPANIES:
        mask = company == handles[name]
        allowed = np.flatnonzero(mask)
        # queries: chunks of this company, perturbed so they aren't exact index members
        q = x[rng.choice(allowed, size=min(200, len(allowed)), replace=False)]
        q = vs.normalize(q + 0.05 * rng.standard_normal(q.shape).astype(np.float32))
        truth = []
        for qi in q:
            s = x[allowed] @ qi
            truth.append(set(allowed[np.argsort(-s)[:K]].tolist()))

        def recall(results):
            return np.mean([len(set(r[0][: K].tolist()) & t) / len(t) for r, t in zip(results, truth)])

        def post(qv):
            ids, _ = idx.search(qv, k=K * OVERFETCH, ef=max(EF, K * OVERFETCH))
            keep = [i for i in ids[0] if i >= 0 and mask[i]][:K]
            return np.array([keep + [-1] * (K - len(keep))])

        strategies = {
            "post": post,
            "in-graph": lambda qv: idx.search(qv, k=K, ef=EF, filter=mask, exact_below=0)[0],
            "exact": lambda qv: idx.search(qv, k=K, filter=mask, exact_below=n)[0],
        }
        for sname, fn in strategies.items():
            fn(q[:1])  # warm-up
            res, lat = timed(fn, q)
            rows.append({"company": name, "allowed": int(mask.sum()), "fraction": float(mask.mean()),
                         "strategy": sname, "recall@10": float(recall(res)),
                         "p50_ms": float(np.percentile(lat, 50)), "p99_ms": float(np.percentile(lat, 99))})
            r = rows[-1]
            print(f"{name:15s} {r['allowed']:7,d} ({r['fraction']:6.2%})  {sname:8s}  "
                  f"recall={r['recall@10']:.3f}  p50={r['p50_ms']:7.2f}ms  p99={r['p99_ms']:7.2f}ms", flush=True)

    out = Path("results")
    out.mkdir(exist_ok=True)
    pd.DataFrame(rows).to_csv(out / "filter_bench.csv", index=False)
    print(f"wrote {out / 'filter_bench.csv'}")


if __name__ == "__main__":
    main()
