"""Samples candidate conversations for writing evaluation questions.

Candidates have one customer, 3-12 turns, and at least one company reply that
says something concrete rather than only routing to DMs. Sampling is spread over
the 30 largest companies so no single brand dominates.

    python eval/sample_candidates.py --per-company 7 > data/eval_candidates.txt
"""
import argparse
import re

import pandas as pd

DEFLECT = re.compile(r"\b(dm|direct message|private message|send us a (?:dm|note|message)|follow us|"
                     r"reach out|contact us|call us|email us|chat with us)\b", re.I)
CONCRETE = re.compile(r"\b(try|go to|settings|update|restart|reinstall|clear|select|tap|click|log ?out|"
                      r"sign ?out|reset|turn (?:off|on)|is available|you can|refund|policy|within \d+|"
                      r"because|due to|known issue|working on|fix|allowed|fee|charge|days?)\b", re.I)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-company", type=int, default=7)
    ap.add_argument("--companies", type=int, default=30)
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()

    conv = pd.read_parquet("data/conversations.parquet", columns=["id", "company_id", "n_turns", "text"])
    tw = pd.read_parquet("data/tweets.parquet", columns=["conversation_id", "author", "inbound", "text"])
    companies = pd.read_parquet("data/companies.parquet")

    n_cust = tw[tw.inbound].groupby("conversation_id")["author"].nunique()
    co = tw[~tw.inbound]
    concrete = co["text"].str.contains(CONCRETE) & ~(co["text"].str.contains(DEFLECT) & (co["text"].str.len() < 140))
    has_concrete = concrete.groupby(co["conversation_id"]).any()

    ok = conv[(conv.n_turns.between(3, 12)) & conv.id.map(n_cust).eq(1) & conv.id.map(has_concrete).fillna(False)]
    top = companies.nlargest(a.companies, "n_conversations")
    picks = (ok[ok.company_id.isin(top.id)]
             .sample(frac=1.0, random_state=a.seed)
             .groupby("company_id").head(a.per_company)
             .sort_values(["company_id", "id"]))
    handle = dict(zip(companies.id, companies.handle))
    print(f"# {len(ok):,} eligible conversations; {len(picks)} sampled", flush=True)
    for r in picks.itertuples():
        print(f"\n=== conv {r.id} [{handle[r.company_id]}] {r.n_turns} turns")
        print(r.text[:900])


if __name__ == "__main__":
    main()
