import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000)


class SearchHit(BaseModel):
    conversation_id: int
    chunk_id: int
    score: float
    company: str
    date: str
    snippet: str


class TweetOut(BaseModel):
    turn: int
    author: str
    inbound: bool
    created_at: datetime
    text: str


class ConversationOut(BaseModel):
    id: int
    company: str
    started_at: datetime
    n_turns: int
    tweets: list[TweetOut]


class RunEventOut(BaseModel):
    seq: int
    type: str
    data: dict


class RunSummary(BaseModel):
    id: uuid.UUID
    created_at: datetime
    question: str
    status: str
    answer: str | None
    answerable: bool | None
    verified: bool | None
    cited_conversation_ids: list[int] | None
    cost_usd: float | None
    latency_s: float | None


class RunOut(RunSummary):
    events: list[RunEventOut]
