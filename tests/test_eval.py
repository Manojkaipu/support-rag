import math

from eval.answer_eval import summarize
from eval.judge_agreement import kappa


def row(id_, answerable, gold, retrieved, cited, grounded, correct, abstained, mode, cost=0.1, lat=10.0):
    return {"id": id_, "answerable": answerable, "gold": gold, "retrieved": retrieved,
            "answer": {"cited_conversation_ids": cited, "verified": grounded, "answer": "x"},
            "grade": {"grounded": grounded, "correct": correct, "abstained": abstained, "failure_mode": mode},
            "usage": {"cost_usd": cost, "latency_s": lat}, "judge_cost": 0.01}


def test_summary_counts():
    rows = [
        row("q1", True, [1], [1, 2], [1], True, True, False, "none"),
        row("q2", True, [3], [4], [4], False, False, False, "retrieval_miss"),
        row("q3", True, [5], [5], [], True, False, True, "wrong_abstention"),
        row("q4", False, [], [9], [], True, True, True, "none"),
    ]
    s = summarize(rows)
    assert "| correct and grounded (answerable) | 33% (1/3) |" in s
    assert "| correct abstention (unanswerable) | 100% (1/1) |" in s
    assert "| wrongly abstained (answerable) | 33% (1/3) |" in s
    assert "| gold conversation retrieved (answerable) | 67% (2/3) |" in s
    assert "| gold conversation cited (answerable) | 33% (1/3) |" in s
    assert "| agent cost | $0.40 total, $0.100 per question |" in s
    assert "| retrieval_miss | 1 |" in s and "| none | 2 |" in s


def test_kappa():
    assert kappa([1, 1, 0, 0], [1, 1, 0, 0]) == 1.0
    assert kappa([1, 0, 1, 0], [0, 1, 0, 1]) == -1.0
    # 3/4 agreement, both 50% positive -> pe = 0.5, kappa = 0.5
    assert math.isclose(kappa([1, 1, 0, 0], [1, 0, 0, 0]), 0.5)
    assert math.isnan(kappa([1, 1], [1, 1]))  # no variation: undefined
