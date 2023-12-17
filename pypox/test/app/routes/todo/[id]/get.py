from sqlite3 import Row
from test.app.database.models import Todo
from test.app.database.session import AsyncSession, dbSession
from test.app.routes.todo.schemas import UserTodo, UserTodoWithId
from sqlmodel import select
from fastapi import Depends, status, HTTPException


async def endpoint(user_id: str, id: str, db: AsyncSession = Depends(dbSession)):
    "get todos"

    # find todo in the database
    todo = (
        await db.execute(select(Todo).where(Todo.id == id, Todo.user_id == user_id))
    ).one()
    return UserTodoWithId(**todo[0].model_dump())

    pass
