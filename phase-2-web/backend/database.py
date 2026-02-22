"""
database.py — Neon DB async connection setup.
Phase II: Full-Stack Web App
"""
import os
import ssl
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set. Copy .env.example to .env and fill it in.")

# asyncpg requires SSL via connect_args, not URL query params
_db_url = DATABASE_URL.split("?")[0]
_ssl_ctx = ssl.create_default_context()

engine = create_async_engine(
    _db_url,
    echo=False,
    connect_args={"ssl": _ssl_ctx},
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def create_tables() -> None:
    """Create all tables in the database."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    """FastAPI dependency — yields a database session."""
    async with AsyncSessionLocal() as session:
        yield session
