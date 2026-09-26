import numpy as np
import pandas as pd

from rag.ingest.conversations import BUDGET, chunk_turns, clean, conversation_keys


def keys_for(rows):
    df = pd.DataFrame(rows, columns=["tweet_id", "author_id", "inbound", "in_response_to_tweet_id"])
    df["in_response_to_tweet_id"] = df["in_response_to_tweet_id"].astype(float)
    key, keep, n_hubs = conversation_keys(df)
    return dict(zip(df["tweet_id"][keep], key[keep].tolist())), n_hubs


def test_clean():
    assert clean("@115712 try this https://t.co/abc @AppleSupport  thanks") == \
        "try this [link] AppleSupport thanks"


def test_plain_thread_and_missing_parent():
    got, n = keys_for([(1, "u1", True, np.nan), (2, "Co", False, 1), (3, "u1", True, 2),
                       (4, "u2", True, 99), (5, "Co", False, 4)])  # 99 isn't in the dump
    assert n == 0
    assert got == {1: 1, 2: 1, 3: 1, 4: 4, 5: 4}


def test_customer_self_reply_is_not_a_hub():
    # the customer adds to their own tweet and the company answers: two authors
    got, n = keys_for([(1, "u1", True, np.nan), (2, "u1", True, 1), (3, "Co", False, 1)])
    assert n == 0 and set(got.values()) == {1}


def test_company_broadcast_root_is_split():
    got, n = keys_for([(10, "Co", False, np.nan), (11, "u1", True, 10), (13, "Co", False, 11),
                       (12, "u2", True, 10), (14, "Co", False, 12),
                       (30, "Co", False, np.nan), (31, "u3", True, 30)])  # single reply: kept
    assert n == 1
    assert got == {11: 11, 13: 11, 12: 12, 14: 12, 30: 30, 31: 30}


def test_viral_and_nested_hubs_are_split():
    # 1 is a viral post (3 distinct repliers). 5 is deeper in a normal thread but draws
    # replies from 3 different customers.
    got, n = keys_for([(1, "ceo", True, np.nan), (2, "u1", True, 1), (3, "u2", True, 1), (4, "u3", True, 1),
                       (20, "u9", True, np.nan), (21, "Co", False, 20), (5, "u9", True, 21),
                       (6, "u4", True, 5), (7, "u5", True, 5), (8, "Co", False, 5), (9, "Co", False, 6)])
    assert n == 2
    assert got[2] == 2 and got[3] == 3 and got[4] == 4 and 1 not in got
    assert got[20] == got[21] == 20 and 5 not in got
    assert got[6] == got[9] == 6 and got[7] == 7 and got[8] == 8


def test_short_conversation_is_one_chunk():
    lines = ["Customer: hi", "Co: hello"]
    assert list(chunk_turns(lines, [3, 3])) == [(0, 1, "Customer: hi\nCo: hello")]


def test_long_conversation_windows():
    n = 12
    lines = [f"turn{i}" for i in range(n)]
    lens = [60] * n
    chunks = list(chunk_turns(lines, lens))
    assert len(chunks) > 1
    covered = set()
    for ts, te, text in chunks:
        assert text.startswith("turn0\n")              # opening message kept as context
        assert 64 + 1 + sum(l + 1 for l in lens[ts:te + 1]) <= BUDGET or ts == te
        covered.update(range(ts, te + 1))
    assert covered == set(range(1, n))
    for (_, prev_end, _), (start, _, _) in zip(chunks, chunks[1:]):
        assert start in (prev_end, prev_end + 1)       # one-turn overlap, always progresses
    assert chunks[-1][1] == n - 1


def test_oversized_turns_still_progress():
    lens = [300, 300, 300, 300]
    chunks = list(chunk_turns(["a", "b", "c", "d"], lens))
    assert [(ts, te) for ts, te, _ in chunks] == [(1, 1), (2, 2), (3, 3)]
