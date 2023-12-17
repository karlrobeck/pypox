from uuid import uuid1
from test.app.database.models import Todo, User
from test.app.database.session import dbSession, AsyncSession
from test.app.routes.todo.schemas import UserTodo
from sqlmodel import select
from fastapi import Depends, HTTPException, status


async def endpoint(user_id: str, body: UserTodo, db: AsyncSession = Depends(dbSession)):
    """
    create a todo
    """

    db.add(Todo(id=str(uuid1()), **body.model_dump(), user_id=user_id))

    await db.commit()

    return "Successfully created"
