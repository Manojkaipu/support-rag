| metric | value |
|---|---|
| questions | 96 (86 answerable, 10 unanswerable) |
| correct and grounded (answerable) | 93% (80/86) |
| grounded (all answers given) | 100% (83/83) |
| correct abstention (unanswerable) | 100% (10/10) |
| wrongly abstained (answerable) | 1% (1/86) |
| gold conversation retrieved (answerable) | 71% (61/86) |
| gold conversation cited (answerable) | 67% (58/86) |
| passed the verifier (after up to 2 revisions) | 93% (87/94) |
| agent cost | $12.65 total, $0.132 per question |
| judge cost | $1.11 |
| latency p50 / p90 | 130.1s / 376.4s |

Failure modes:

| mode | count |
|---|---|
| none | 87 |
| retrieval_miss | 4 |
| unsupported_claim | 3 |
| agent_error | 2 |
