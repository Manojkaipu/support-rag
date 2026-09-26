import numpy as np

from rag.retrieval import collapse


def test_collapse_keeps_best_chunk_per_conversation():
    chunk_conv = np.array([0, 0, 1, 2, 2, 3])
    assert collapse([4, 1, 0, 3, 2, -1], chunk_conv, k=10) == [(2, 4), (0, 1), (1, 2)]
    assert collapse([5, 4, 3], chunk_conv, k=1) == [(3, 5)]
