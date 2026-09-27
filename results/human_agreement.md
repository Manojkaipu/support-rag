10 hand-graded answers (answers the judges disagreed on were sampled first).

### Human vs first judge (Grok)

| dimension | agreement | Cohen's kappa |
|---|---|---|
| grounded | 50% | 0.00 |
| correct | 90% | 0.00 |
| abstained | 100% | 1.00 |

Disagreements:
- q017 ['grounded']: judge said 'The answer states the reference’s key point—the lock lasts 24 hours after the last failed attempt and further wrong attempts can lock it again—and every extra detail (no temporary password, Online Support number, DM/reset variations, booking workaround) is supported by the cited Delta agents.'; notes: "includes a customer's report (labelled as such); strict rule: only agent statements count as grounded"
- q092 ['grounded']: judge said "The system correctly declined, stating that FedEx is absent from the support history and that other carriers' policies cannot be substituted, which matches the reference for this unanswerable question."; notes: 'correctly declined and refused to substitute; strict rule: uncited remarks about what the data contains count as ungrounded'
- q096 ['grounded']: judge said 'The system correctly declined, stating that the 2017 support history does not cover Disney+ or how to cancel a Disney+ subscription, and it did not substitute unrelated services’ policies.'; notes: 'correctly declined and refused to substitute; strict rule: uncited remarks about what the data contains count as ungrounded'
- q035 ['correct']: judge said 'Every claim in the system answer is supported by 2017 BA agent statements in the cited threads, but the answer omits the reference’s key point that oversold flights are handled by first seeking volunteers and then selecting passengers.'; notes: 'answers the why; volunteers/selection detail is secondary'
- q100 ['grounded']: judge said 'The question is unanswerable from the 2017 support history, and the system correctly declined, stating that Zoom is not covered and that no agent reply gives a free-meeting time limit. It makes no unsupported policy claim.'; notes: 'correctly declined and refused to substitute; strict rule: uncited remarks about what the data contains count as ungrounded'
- q079 ['grounded']: judge said 'The answer correctly reports that O2 attributed the failed discount to codes running out quickly because the offer was popular, and the extra day-specific explanations are directly supported by the cited agent replies.'; notes: 'last sentence asserts the rules no longer apply: an uncited inference beyond the allowed 2017 caveat'

### Human vs second judge (OpenAI)

| dimension | agreement | Cohen's kappa |
|---|---|---|
| grounded | 100% | 1.00 |
| correct | 80% | 0.00 |
| abstained | 100% | 1.00 |

Disagreements:
- q047 ['correct']: judge said 'The answer accurately reports Hulu’s restart and troubleshooting-link advice, along with the request for a photo if trouble recurred. It omits the customer’s finding that the problem appeared limited to one season.'; notes: ''
- q012 ['correct']: judge said 'The cited support agents gave the troubleshooting advice listed. However, the answer omits the key resolution in the matching conversation: the customer fixed the issue by refreshing the tab.'; notes: 'agent advice answers the question; the refresh fix came from the customer (same pattern as q047)'
