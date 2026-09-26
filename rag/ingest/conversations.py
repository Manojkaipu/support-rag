"""twcs.csv -> conversations and chunks (parquet + numpy in data_dir), then Postgres.

A conversation is a reply thread, found by following in_response_to_tweet_id up
to the root or to the first hub (see conversation_keys). Only threads with both
a customer and a company tweet are kept. Turns are ordered by timestamp.

Chunks fit MiniLM's 256-token window. Short conversations are one chunk; long
ones become windows of whole turns overlapping by one turn, each prefixed with
the customer's opening message so it keeps the topic.

    python -m rag.ingest.conversations --csv twcs.csv
"""
import argparse
import re
import time

import numpy as np
import pandas as pd
from sqlalchemy import create_engine

from rag.config import settings
from rag.db.models import CORPUS_TABLES, Base

BUDGET = 240       # tokens per chunk, leaving room for [CLS]/[SEP]
HEAD_TOKENS = 64   # opening message budget in continuation chunks
HEAD_CHARS = 250   # ~64 tokens of tweet text

URL = re.compile(r"https?://\S+")
USER_MENTION = re.compile(r"@\d+\b")   # customers are anonymized to numeric ids
MENTION = re.compile(r"@(\w+)")
SPACE = re.compile(r"\s+")


def clean(text: str) -> str:
    text = URL.sub("[link]", text)
    text = USER_MENTION.sub(" ", text)
    text = MENTION.sub(r"\1", text)
    return SPACE.sub(" ", text).strip()


def conversation_keys(df):
    """Assigns each tweet a conversation key and drops hub tweets.

    Some tweets collect replies from many unrelated people: company broadcasts
    ("Welcome! Follow us"), viral posts, status updates. Following reply links
    would merge all of those threads into one. A hub is a tweet whose direct
    replies come from 3+ distinct authors, or a company-authored root with 2+
    replies. Each reply to a hub starts its own conversation; the hub is dropped.
    Expects columns tweet_id, author_id, inbound, in_response_to_tweet_id.
    """
    ids = df["tweet_id"].to_numpy()
    known = set(ids.tolist())
    par = df["in_response_to_tweet_id"].to_numpy()
    parent = {i: int(p) for i, p in zip(ids.tolist(), par.tolist())
              if not np.isnan(p) and int(p) in known}
    replies = df[df["tweet_id"].isin(parent.keys())].assign(
        parent=lambda d: d["tweet_id"].map(parent))
    fan = replies.groupby("parent")["author_id"].agg(["nunique", "size"])
    hubs = set(fan.index[fan["nunique"] >= 3])
    company_roots = df.loc[~df["inbound"] & ~df["tweet_id"].isin(parent.keys()), "tweet_id"]
    hubs |= set(fan.index[(fan["size"] >= 2) & fan.index.isin(company_roots)])

    key = {}
    for start in ids.tolist():
        path, i = [], start
        while True:
            if i in key:
                k = key[i]
                break
            p = parent.get(i)
            if p is None or p in hubs:
                k = i
                key[i] = k
                break
            path.append(i)
            i = p
        for x in path:
            key[x] = k
    keys = np.array([key[i] for i in ids.tolist()], dtype=np.int64)
    keep = ~np.isin(ids, list(hubs))
    return keys, keep, len(hubs)


def chunk_turns(lines, lens):
    """Yields (turn_start, turn_end, text); lens are token counts per line."""
    if sum(lens) + len(lens) <= BUDGET:
        yield 0, len(lines) - 1, "\n".join(lines)
        return
    head = lines[0][:HEAD_CHARS]
    head_len = min(lens[0], HEAD_TOKENS) + 1
    start = 1
    while True:
        end, used = start, head_len + lens[start] + 1
        while end + 1 < len(lines) and used + lens[end + 1] + 1 <= BUDGET:
            end += 1
            used += lens[end] + 1
        yield start, end, "\n".join([head] + lines[start:end + 1])
        if end == len(lines) - 1:
            return
        start = end if end > start else end + 1


def build(csv_path, out):
    t0 = time.time()
    df = pd.read_csv(csv_path, usecols=["tweet_id", "author_id", "inbound", "created_at", "text",
                                        "in_response_to_tweet_id"],
                     dtype={"tweet_id": np.int64, "author_id": str, "inbound": bool, "text": str})
    df["text"] = df["text"].fillna("").str.replace("\x00", "", regex=False)  # Postgres rejects NUL
    df["created_at"] = pd.to_datetime(df["created_at"], format="%a %b %d %H:%M:%S %z %Y")
    key, keep_rows, n_hubs = conversation_keys(df)
    df["root"] = key
    df = df[keep_rows]
    print(f"dropped {n_hubs:,} hub tweets; their replies start separate conversations", flush=True)

    g = df.groupby("root")["inbound"]
    keep = g.any() & ~g.all()
    df = df[df["root"].isin(keep[keep].index)]

    company_of = (df[~df["inbound"]].groupby("root")["author_id"]
                  .agg(lambda s: s.value_counts().index[0]))
    handles = company_of.value_counts()
    companies = pd.DataFrame({"id": np.arange(len(handles), dtype=np.int16),
                              "handle": handles.index.to_numpy(), "n_conversations": handles.to_numpy()})

    span = df.groupby("root")["created_at"].agg(["min", "max", "size"])
    span = span.sort_values(["min"], kind="stable")
    span["id"] = np.arange(len(span), dtype=np.int32)
    span["company_id"] = company_of.reindex(span.index).map(dict(zip(companies["handle"], companies["id"])))

    df["conversation_id"] = span["id"].reindex(df["root"]).to_numpy()
    df = df.sort_values(["conversation_id", "created_at", "tweet_id"], kind="stable").reset_index(drop=True)
    df["turn"] = df.groupby("conversation_id").cumcount()
    df["line"] = np.where(df["inbound"], "Customer", df["author_id"]) + ": " + df["text"].map(clean)
    print(f"{len(df):,} tweets, {len(span):,} conversations, {len(companies)} companies "
          f"({time.time() - t0:.0f}s)", flush=True)

    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(settings.embed_model)
    lines = df["line"].tolist()
    lens = np.empty(len(lines), dtype=np.int32)
    for s in range(0, len(lines), 100_000):
        ids = tok(lines[s:s + 100_000], add_special_tokens=False)["input_ids"]
        lens[s:s + len(ids)] = [len(x) for x in ids]
    print(f"tokenized ({time.time() - t0:.0f}s)", flush=True)

    bounds = np.flatnonzero(np.r_[True, np.diff(df["conversation_id"].to_numpy()) != 0, True])
    rows = []
    for c in range(len(bounds) - 1):
        lo, hi = bounds[c], bounds[c + 1]
        for ts, te, text in chunk_turns(lines[lo:hi], lens[lo:hi].tolist()):
            rows.append((c, ts, te, text))
    chunks = pd.DataFrame(rows, columns=["conversation_id", "turn_start", "turn_end", "text"])
    chunks.insert(0, "id", np.arange(len(chunks), dtype=np.int32))
    print(f"{len(chunks):,} chunks, {(chunks.groupby('conversation_id').size() > 1).mean():.1%} of "
          f"conversations split ({time.time() - t0:.0f}s)", flush=True)

    conv_text = df.groupby("conversation_id")["line"].agg("\n".join)
    conversations = pd.DataFrame({
        "id": span["id"].to_numpy(), "root_tweet_id": span.index.to_numpy(),
        "company_id": span["company_id"].to_numpy(np.int16), "started_at": span["min"].to_numpy(),
        "ended_at": span["max"].to_numpy(), "n_turns": span["size"].to_numpy(np.int16),
        "text": conv_text.reindex(span["id"]).to_numpy()})
    tweets = df.rename(columns={"tweet_id": "id", "author_id": "author"})[
        ["id", "conversation_id", "turn", "author", "inbound", "created_at", "text"]]

    out.mkdir(parents=True, exist_ok=True)
    companies.to_parquet(out / "companies.parquet")
    conversations.to_parquet(out / "conversations.parquet")
    tweets.to_parquet(out / "tweets.parquet")
    chunks.to_parquet(out / "chunks.parquet")
    np.save(out / "chunk_conversation.npy", chunks["conversation_id"].to_numpy(np.int32))
    np.save(out / "chunk_company.npy",
            conversations["company_id"].to_numpy()[chunks["conversation_id"].to_numpy()].astype(np.int16))
    print(f"wrote {out} ({time.time() - t0:.0f}s)", flush=True)
    return companies, conversations, tweets, chunks


def copy_frame(cur, table, frame):
    cols = ", ".join(frame.columns)
    with cur.copy(f"COPY {table} ({cols}) FROM STDIN") as cp:
        for row in frame.itertuples(index=False, name=None):
            cp.write_row(row)


def load_db(companies, conversations, tweets, chunks):
    t0 = time.time()
    engine = create_engine(settings.database_url)
    Base.metadata.drop_all(engine, tables=CORPUS_TABLES)  # leaves run history alone
    Base.metadata.create_all(engine)
    raw = engine.raw_connection()
    try:
        with raw.cursor() as cur:
            for table, frame in [("companies", companies), ("conversations", conversations),
                                 ("tweets", tweets), ("chunks", chunks)]:
                copy_frame(cur, table, frame)
                print(f"  {table}: {len(frame):,} rows ({time.time() - t0:.0f}s)", flush=True)
        raw.commit()
    finally:
        raw.close()
    with engine.begin() as conn:
        conn.exec_driver_sql("ANALYZE")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="twcs.csv")
    ap.add_argument("--skip-db", action="store_true")
    a = ap.parse_args()
    frames = build(a.csv, settings.data_dir)
    if not a.skip_db:
        load_db(*frames)


if __name__ == "__main__":
    main()
