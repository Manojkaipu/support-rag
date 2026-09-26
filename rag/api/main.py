"""HTTP API.

    uvicorn rag.api.main:app --port 8000
"""
import asyncio
import json
import time
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from prometheus_client import make_asgi_app
from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from rag.api.schemas import AskRequest, ConversationOut, RunOut, RunSummary, SearchHit, TweetOut
from rag.config import settings
from rag.db.models import Base, Company, Conversation, Run, RunEvent
from rag.db.session import make_db
from rag.observability import record_run, setup_tracing
from rag.retrieval import MODES


def sse(event: str, data: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(data, default=str)}\n\n"


def create_app(retriever=None, agent=None, database_url: str | None = None) -> FastAPI:
    """Real retriever and agent are built at startup unless passed in (tests pass fakes)."""

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        engine, sessionmaker = make_db(database_url)
        SQLAlchemyInstrumentor().instrument(engine=engine.sync_engine)
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        r = retriever
        if r is None:
            from rag.retrieval import Retriever
            r = await asyncio.to_thread(Retriever)
        a = agent
        if a is None:
            from rag.agent import Agent
            a = Agent(r, sessionmaker)
        app.state.retriever, app.state.agent, app.state.sessionmaker = r, a, sessionmaker
        yield
        await engine.dispose()

    app = FastAPI(title="support-rag", lifespan=lifespan)
    app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origins, allow_methods=["*"],
                       allow_headers=["*"])
    app.mount("/metrics", make_asgi_app())
    FastAPIInstrumentor.instrument_app(app, excluded_urls="healthz,metrics")

    @app.get("/healthz")
    async def healthz():
        return {"ok": True}

    @app.get("/api/companies")
    async def companies(request: Request):
        async with request.app.state.sessionmaker() as s:
            rows = await s.execute(select(Company.handle, Company.n_conversations)
                                   .order_by(Company.n_conversations.desc()))
        return [{"handle": h, "conversations": n} for h, n in rows]

    @app.get("/api/search", response_model=list[SearchHit])
    async def search(request: Request, q: str = Query(min_length=2), company: str | None = None,
                     mode: str = "hybrid", k: int = Query(10, ge=1, le=50)):
        if mode not in MODES:
            raise HTTPException(422, f"mode must be one of {MODES}")
        r = request.app.state.retriever
        try:
            hits = await asyncio.to_thread(r.search, q, k, mode, company)
        except KeyError as e:
            raise HTTPException(404, str(e)) from e
        return await asyncio.to_thread(r.describe, hits)

    @app.get("/api/conversations/{conversation_id}", response_model=ConversationOut)
    async def conversation(request: Request, conversation_id: int):
        async with request.app.state.sessionmaker() as s:
            c = await s.scalar(select(Conversation).where(Conversation.id == conversation_id)
                               .options(selectinload(Conversation.tweets), selectinload(Conversation.company)))
        if c is None:
            raise HTTPException(404, "conversation not found")
        return ConversationOut(id=c.id, company=c.company.handle, started_at=c.started_at, n_turns=c.n_turns,
                               tweets=[TweetOut(turn=t.turn, author=t.author, inbound=t.inbound,
                                                created_at=t.created_at, text=t.text) for t in c.tweets])

    @app.post("/api/ask")
    async def ask(request: Request, body: AskRequest):
        state = request.app.state
        async with state.sessionmaker() as s:
            run = Run(id=uuid.uuid4(), question=body.question, status="running")
            s.add(run)
            await s.commit()

        async def stream():
            events, final, usage = [], None, {}
            t0 = time.perf_counter()
            yield sse("run", {"run_id": str(run.id)})
            try:
                async for ev in state.agent.run(body.question):
                    events.append(ev)
                    if ev.type == "answer":
                        final = ev.data
                    elif ev.type == "usage":
                        usage = ev.data
                    yield sse(ev.type, ev.data)
            finally:
                # also runs when the client disconnects and the stream is cancelled
                record_run(events, time.perf_counter() - t0)
                await asyncio.shield(save(state.sessionmaker, run.id, events, final, usage))

        return StreamingResponse(stream(), media_type="text/event-stream",
                                 headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})

    @app.get("/api/runs", response_model=list[RunSummary])
    async def runs(request: Request, limit: int = Query(20, ge=1, le=100)):
        async with request.app.state.sessionmaker() as s:
            rows = await s.scalars(select(Run).order_by(Run.created_at.desc()).limit(limit))
            return [RunSummary.model_validate(r, from_attributes=True) for r in rows]

    @app.get("/api/runs/{run_id}", response_model=RunOut)
    async def get_run(request: Request, run_id: uuid.UUID):
        async with request.app.state.sessionmaker() as s:
            r = await s.scalar(select(Run).where(Run.id == run_id).options(selectinload(Run.events)))
            if r is None:
                raise HTTPException(404, "run not found")
            return RunOut.model_validate(r, from_attributes=True)

    @app.get("/api/stats")
    async def stats(request: Request):
        async with request.app.state.sessionmaker() as s:
            row = (await s.execute(select(func.count(), func.avg(Run.cost_usd), func.avg(Run.latency_s))
                                   .where(Run.status == "answered"))).one()
        return {"answered_runs": row[0], "avg_cost_usd": row[1], "avg_latency_s": row[2]}

    return app


async def save(sessionmaker, run_id, events, final, usage):
    async with sessionmaker() as s:
        run = await s.get(Run, run_id)
        run.status = "answered" if final else "failed"
        if final:
            run.answer, run.answerable = final["answer"], final["answerable"]
            run.verified, run.cited_conversation_ids = final["verified"], final["cited_conversation_ids"]
        run.cost_usd, run.latency_s = usage.get("cost_usd"), usage.get("latency_s")
        s.add_all(RunEvent(run_id=run_id, seq=i, type=e.type, data=json.loads(json.dumps(e.data, default=str)))
                  for i, e in enumerate(events))
        await s.commit()


setup_tracing()
app = create_app()
