from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from rag.config import settings


def make_db(url: str | None = None):
    """Engine + session factory. Create inside the event loop that will use them."""
    engine = create_async_engine(url or settings.database_url, pool_size=10, pool_pre_ping=True)
    return engine, async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
