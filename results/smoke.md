| metric | value |
|---|---|
| questions | 5 (4 answerable, 1 unanswerable) |
| correct and grounded (answerable) | 100% (4/4) |
| grounded (all answers given) | 100% (4/4) |
| correct abstention (unanswerable) | 100% (1/1) |
| wrongly abstained (answerable) | 0% (0/4) |
| gold conversation retrieved (answerable) | 50% (2/4) |
| gold conversation cited (answerable) | 50% (2/4) |
| verifier accepted first draft | 80% (4/5) |
| agent cost | $0.42 total, $0.083 per question |
| judge cost | $0.04 |
| latency p50 / p90 | 46.4s / 343.8s |

Failure modes:

| mode | count |
|---|---|
| none | 4 |
| unsupported_claim | 1 |
