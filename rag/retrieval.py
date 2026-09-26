"""Hybrid retrieval over conversation chunks.

Both indexes return chunks; results are collapsed to conversations (best-ranked
chunk wins) before reciprocal rank fusion, so a conversation split into several
chunks can't take several slots.
"""
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

import vecsearch as vs
from rag.config import settings
from rag.observability import RETRIEVAL_SECONDS, tracer


def timed_stage(stage):
    """Span + latency histogram around one retrieval stage."""
    def wrap(fn):
        def inner(*a, **kw):
            with tracer.start_as_current_span(f"retrieval.{stage}"), RETRIEVAL_SECONDS.labels(stage).time():
                return fn(*a, **kw)
        return inner
    return wrap

MODES = ("vector", "bm25", "hybrid")


@dataclass
class Hit:
    conversation_id: int
    chunk_id: int
    score: float


def collapse(chunk_ids, chunk_conv, k):
    """Chunk ranking -> conversation ranking, keeping each conversation's best chunk."""
    seen, out = set(), []
    for c in chunk_ids:
        if c < 0:
            continue
        conv = int(chunk_conv[c])
        if conv not in seen:
            seen.add(conv)
            out.append((conv, int(c)))
            if len(out) == k:
                break
    return out


class Retriever:
    # exact_below: with a company filter, scan the allowed chunks exactly when there are at most
    # this many. bench/filter_bench.py puts the crossover with in-graph filtering near 5k chunks.
    def __init__(self, data_dir: Path | None = None, ef: int = 128, exact_below: int = 5_000):
        from sentence_transformers import SentenceTransformer

        d = Path(data_dir or settings.data_dir)
        self.hnsw = vs.HNSWIndex.load(str(d / "hnsw.bin"))
        self.bm25 = vs.BM25Index.load(str(d / "bm25.bin"))
        self.chunk_conv = np.load(d / "chunk_conversation.npy")
        self.chunk_company = np.load(d / "chunk_company.npy")
        self.chunk_text = pd.read_parquet(d / "chunks.parquet", columns=["text"])["text"].to_numpy()
        self.conv_started = pd.read_parquet(d / "conversations.parquet", columns=["started_at"])["started_at"].to_numpy()
        companies = pd.read_parquet(d / "companies.parquet")
        self.company_id_by_handle = dict(zip(companies.handle, companies.id))
        self.company_id = {h.lower(): i for h, i in self.company_id_by_handle.items()}
        self.handle = dict(zip(companies.id, companies.handle))
        self.model = SentenceTransformer(settings.embed_model)
        self.ef, self.exact_below = ef, exact_below

    def company_mask(self, company: str | None):
        if company is None:
            return None
        cid = self.company_id.get(company.lower())
        if cid is None:
            raise KeyError(f"unknown company {company!r}")
        return self.chunk_company == cid

    def describe(self, hits: list[Hit]) -> list[dict]:
        return [{"conversation_id": h.conversation_id, "chunk_id": h.chunk_id, "score": round(h.score, 4),
                 "company": self.handle[int(self.chunk_company[h.chunk_id])],
                 "date": str(pd.Timestamp(self.conv_started[h.conversation_id]).date()),
                 "snippet": str(self.chunk_text[h.chunk_id])} for h in hits]

    def embed(self, text: str) -> np.ndarray:
        return self.model.encode([text], normalize_embeddings=True, convert_to_numpy=True)

    @timed_stage("vector")
    def vector(self, query, k, mask=None, pool=100):
        ids, dist = self.hnsw.search(self.embed(query), k=pool, ef=max(self.ef, pool),
                                     filter=mask, exact_below=self.exact_below)
        convs = collapse(ids[0], self.chunk_conv, k)
        score = {int(c): 1.0 - float(d) for c, d in zip(ids[0], dist[0]) if c >= 0}
        return [Hit(conv, ch, score[ch]) for conv, ch in convs]

    @timed_stage("bm25")
    def lexical(self, query, k, mask=None, pool=100):
        ids, scores = self.bm25.search(query, k=pool, filter=mask)
        convs = collapse(ids[0], self.chunk_conv, k)
        score = {int(c): float(s) for c, s in zip(ids[0], scores[0]) if c >= 0}
        return [Hit(conv, ch, score[ch]) for conv, ch in convs]

    def search(self, query: str, k: int = 10, mode: str = "hybrid", company: str | None = None,
               pool: int = 100) -> list[Hit]:
        if mode not in MODES:
            raise ValueError(f"mode must be one of {MODES}")
        with tracer.start_as_current_span("retrieval.search") as span:
            span.set_attributes({"rag.mode": mode, "rag.company": company or "any", "rag.k": k})
            mask = self.company_mask(company)
            if mode == "vector":
                hits = self.vector(query, k, mask, pool)
            elif mode == "bm25":
                hits = self.lexical(query, k, mask, pool)
            else:
                v, b = self.vector(query, pool, mask, pool), self.lexical(query, pool, mask, pool)
                hits = self.fuse(v, b, k)
            span.set_attribute("rag.hits", len(hits))
            return hits

    @timed_stage("fuse")
    def fuse(self, v, b, k):
        best_chunk = {h.conversation_id: h.chunk_id for h in b}
        best_chunk.update({h.conversation_id: h.chunk_id for h in v})  # prefer the semantic match
        ids, scores = vs.rrf([[h.conversation_id for h in v], [h.conversation_id for h in b]], k=k)
        return [Hit(c, best_chunk[c], s) for c, s in zip(ids, scores)]
