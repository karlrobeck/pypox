import asyncio
from typing import Optional
from sqlmodel import Field, SQLModel
from uuid import uuid1
from sqlalchemy.ext.asyncio import create_async_engine


class Todo(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: bool
    user_id: Optional[str] = Field(default=None, foreign_key="user.id")


class User(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    username: str
    password: str
    name: str
    email: str
    phone: str


async_engine = create_async_engine("sqlite+aiosqlite:///test/database.db")


async def createTable():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(createTable())
