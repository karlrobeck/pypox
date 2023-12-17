import asyncio
from typing import AsyncGenerator
from click import Context
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from pypox.database import create_engine_async, init_database_async, AsyncEngine
from test.app.database.SQLITE import TodoDatabase
from contextvars import ContextVar

engine: ContextVar[AsyncEngine] = ContextVar("engine")


async def dbSession() -> AsyncSession:  # type: ignore
    async with AsyncSession(engine.get()) as session:
        async with session.begin():
            yield session  # type: ignore


def __call__(app: FastAPI) -> None:
    # create async engine
    engine.set(create_engine_async(TodoDatabase, "aiosqlite"))
    asyncio.run(init_database_async(engine.get(), TodoDatabase))
