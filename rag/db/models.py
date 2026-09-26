"""Corpus tables. Conversation and chunk ids are dense (0..n-1) because they
double as row ids in the vector and BM25 indexes."""
import uuid
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, Float, ForeignKey, Integer, SmallInteger, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    handle: Mapped[str] = mapped_column(String(64), unique=True)
    n_conversations: Mapped[int] = mapped_column(Integer)


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    root_tweet_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    ended_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    n_turns: Mapped[int] = mapped_column(SmallInteger)
    text: Mapped[str] = mapped_column(Text)  # rendered "Speaker: message" lines, cleaned

    company: Mapped[Company] = relationship()
    tweets: Mapped[list["Tweet"]] = relationship(order_by="Tweet.turn", back_populates="conversation")


class Tweet(Base):
    __tablename__ = "tweets"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"), index=True)
    turn: Mapped[int] = mapped_column(SmallInteger)
    author: Mapped[str] = mapped_column(String(64))
    inbound: Mapped[bool] = mapped_column(Boolean)  # True = customer
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    text: Mapped[str] = mapped_column(Text)  # raw

    conversation: Mapped[Conversation] = relationship(back_populates="tweets")


class Chunk(Base):
    __tablename__ = "chunks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=False)
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"), index=True)
    turn_start: Mapped[int] = mapped_column(SmallInteger)
    turn_end: Mapped[int] = mapped_column(SmallInteger)  # inclusive
    text: Mapped[str] = mapped_column(Text)


CORPUS_TABLES = [Company.__table__, Conversation.__table__, Tweet.__table__, Chunk.__table__]


class Run(Base):
    """One question answered by the agent."""
    __tablename__ = "runs"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), index=True)
    question: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(16), default="running")  # running | answered | failed
    answer: Mapped[str | None] = mapped_column(Text)
    answerable: Mapped[bool | None] = mapped_column(Boolean)
    verified: Mapped[bool | None] = mapped_column(Boolean)
    cited_conversation_ids: Mapped[list | None] = mapped_column(JSONB)
    cost_usd: Mapped[float | None] = mapped_column(Float)
    latency_s: Mapped[float | None] = mapped_column(Float)

    events: Mapped[list["RunEvent"]] = relationship(order_by="RunEvent.seq", cascade="all, delete-orphan")


class RunEvent(Base):
    __tablename__ = "run_events"

    run_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("runs.id", ondelete="CASCADE"), primary_key=True)
    seq: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[str] = mapped_column(String(16))
    data: Mapped[dict] = mapped_column(JSONB)
