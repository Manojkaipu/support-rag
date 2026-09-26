"""API tests against a real Postgres (TEST_DATABASE_URL) with fake retriever and agent."""
import json
import os
from datetime import datetime, timezone

import pytest
from sqlalchemy import create_engine, text

from rag.agent import Event
from rag.db.models import Base, Company, Conversation, Tweet
from rag.retrieval import Hit

URL = os.environ.get("TEST_DATABASE_URL")
pytestmark = pytest.mark.skipif(not URL, reason="TEST_DATABASE_URL not set")


class FakeRetriever:
    def search(self, q, k, mode, company):
        if company == "Nope":
            raise KeyError("unknown company 'Nope'")
        return [Hit(7, 70, 0.5)]

    def describe(self, hits):
        return [{"conversation_id": 7, "chunk_id": 70, "score": 0.5, "company": "Delta", "date": "2017-11-01",
                 "snippet": "Delta: locked for 24 hours"}]


class FakeAgent:
    def __init__(self, fail=False):
        self.fail = fail

    async def run(self, question):
        yield Event("text", {"text": "Searching Delta."})
        yield Event("tool_call", {"id": "t1", "name": "search_conversations", "input": {"query": question}})
        if self.fail:
            yield Event("error", {"reason": "max_turns"})
        else:
            yield Event("answer", {"answer": "24 hours [#7].", "cited_conversation_ids": [7], "answerable": True,
                                   "verified": True, "verification": {"supported": True}})
        yield Event("usage", {"cost_usd": 0.012, "latency_s": 3.4})


@pytest.fixture(scope="module")
def seeded():
    eng = create_engine(URL)
    Base.metadata.drop_all(eng)
    Base.metadata.create_all(eng)
    t0 = datetime(2017, 11, 1, 12, tzinfo=timezone.utc)
    with eng.begin() as c:
        c.execute(Company.__table__.insert(), [{"id": 0, "handle": "Delta", "n_conversations": 1}])
        c.execute(Conversation.__table__.insert(), [{"id": 7, "root_tweet_id": 100, "company_id": 0,
                                                     "started_at": t0, "ended_at": t0, "n_turns": 2,
                                                     "text": "Customer: locked out\nDelta: 24 hours"}])
        c.execute(Tweet.__table__.insert(), [
            {"id": 100, "conversation_id": 7, "turn": 0, "author": "u1", "inbound": True, "created_at": t0,
             "text": "@Delta locked out"},
            {"id": 101, "conversation_id": 7, "turn": 1, "author": "Delta", "inbound": False, "created_at": t0,
             "text": "@u1 24 hours"}])
    yield eng
    eng.dispose()


def client_for(agent):
    from fastapi.testclient import TestClient

    from rag.api.main import create_app
    return TestClient(create_app(retriever=FakeRetriever(), agent=agent, database_url=URL))


def parse_sse(body: str):
    out = []
    for block in body.strip().split("\n\n"):
        lines = dict(line.split(": ", 1) for line in block.split("\n"))
        out.append((lines["event"], json.loads(lines["data"])))
    return out


def test_read_endpoints(seeded):
    with client_for(FakeAgent()) as c:
        assert c.get("/healthz").json() == {"ok": True}
        assert c.get("/api/companies").json() == [{"handle": "Delta", "conversations": 1}]
        conv = c.get("/api/conversations/7").json()
        assert conv["company"] == "Delta" and [t["turn"] for t in conv["tweets"]] == [0, 1]
        assert c.get("/api/conversations/999").status_code == 404
        hits = c.get("/api/search", params={"q": "locked", "company": "Delta"}).json()
        assert hits[0]["conversation_id"] == 7
        assert c.get("/api/search", params={"q": "locked", "company": "Nope"}).status_code == 404
        assert c.get("/api/search", params={"q": "locked", "mode": "magic"}).status_code == 422


def test_ask_streams_and_persists(seeded):
    with client_for(FakeAgent()) as c:
        r = c.post("/api/ask", json={"question": "How long is a Delta lockout?"})
        assert r.headers["content-type"].startswith("text/event-stream")
        events = parse_sse(r.text)
        assert [e for e, _ in events] == ["run", "text", "tool_call", "answer", "usage"]
        run_id = events[0][1]["run_id"]
        run = c.get(f"/api/runs/{run_id}").json()
        assert run["status"] == "answered" and run["verified"] and run["cited_conversation_ids"] == [7]
        assert run["cost_usd"] == pytest.approx(0.012)
        assert [e["type"] for e in run["events"]] == ["text", "tool_call", "answer", "usage"]
        assert c.get("/api/runs").json()[0]["id"] == run_id


def test_failed_run_is_recorded(seeded):
    with client_for(FakeAgent(fail=True)) as c:
        events = parse_sse(c.post("/api/ask", json={"question": "anything at all?"}).text)
        run = c.get(f"/api/runs/{events[0][1]['run_id']}").json()
        assert run["status"] == "failed" and run["answer"] is None


def test_init_db_waits_for_the_database(monkeypatch):
    import asyncio

    from sqlalchemy.exc import OperationalError

    from rag.api import main

    calls = []

    class FlakyEngine:
        def begin(self):
            calls.append(1)
            if len(calls) < 3:
                raise OperationalError("connect", {}, Exception("failed to resolve host 'postgres'"))
            return self

        async def __aenter__(self):
            return self

        async def __aexit__(self, *exc):
            return False

        async def run_sync(self, fn):
            pass

    asyncio.run(main.init_db(FlakyEngine(), attempts=5, delay=0))
    assert len(calls) == 3
    calls.clear()
    with pytest.raises(OperationalError):
        asyncio.run(main.init_db(FlakyEngine(), attempts=2, delay=0))


def test_validation(seeded):
    with client_for(FakeAgent()) as c:
        assert c.post("/api/ask", json={"question": "?"}).status_code == 422
