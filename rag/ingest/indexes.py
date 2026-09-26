"""Builds the retrieval indexes over data/chunks.parquet.

    python -m rag.ingest.indexes bm25
    python -m rag.ingest.indexes embed   # resumable; then builds the HNSW graph

Row i of every index is chunk id i.
"""
import argparse
import os
import time

import numpy as np
import pandas as pd

import vecsearch as vs
from rag.config import settings

DIM = 384
BLOCK = 20_000


def build_bm25(d):
    texts = pd.read_parquet(d / "chunks.parquet", columns=["text"])["text"].tolist()
    t = time.time()
    idx = vs.BM25Index()
    idx.add(texts)
    idx.save(str(d / "bm25.bin"))
    print(f"bm25: {len(idx):,} docs, {idx.vocab_size:,} terms, {time.time() - t:.0f}s, "
          f"{os.path.getsize(d / 'bm25.bin') / 2**20:.0f} MB", flush=True)


def embed(d):
    from sentence_transformers import SentenceTransformer

    texts = pd.read_parquet(d / "chunks.parquet", columns=["text"])["text"].tolist()
    n = len(texts)
    path, done_path = d / "chunk_emb.f32", d / "chunk_emb.f32.done"
    mm = np.memmap(path, dtype=np.float32, mode="r+" if path.exists() else "w+", shape=(n, DIM))
    start = int(done_path.read_text()) if done_path.exists() else 0
    model = SentenceTransformer(settings.embed_model)
    t = time.time()
    for s in range(start, n, BLOCK):
        e = min(s + BLOCK, n)
        mm[s:e] = model.encode(texts[s:e], batch_size=64, normalize_embeddings=True,
                               convert_to_numpy=True, show_progress_bar=False)
        mm.flush()
        done_path.write_text(str(e))
        rate = (e - start) / (time.time() - t)
        print(f"embedded {e:,}/{n:,}  {rate:.0f}/s  eta {(n - e) / rate / 60:.0f} min", flush=True)
    del mm

    x = np.fromfile(path, dtype=np.float32).reshape(n, DIM)
    t = time.time()
    idx = vs.HNSWIndex(DIM, n, "ip", M=16, ef_construction=200)
    idx.add(x, num_threads=os.cpu_count())
    idx.save(str(d / "hnsw.bin"))
    print(f"hnsw: {n:,} vectors built in {time.time() - t:.0f}s", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["bm25", "embed"])
    a = ap.parse_args()
    {"bm25": build_bm25, "embed": embed}[a.what](settings.data_dir)


if __name__ == "__main__":
    main()
