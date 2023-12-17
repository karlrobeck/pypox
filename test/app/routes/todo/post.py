from uuid import uuid1
from test.app.database.SQLITE import TodoDatabase
from test.app.routes.todo.schemas import UserTodo
from sqlmodel import select
from fastapi import Depends, HTTPException, status
from pypox.database import asyncDbSession, AsyncSession


async def endpoint(user_id: str, body: UserTodo):
    """
    create a todo
    """
    async with await asyncDbSession(TodoDatabase) as session:
        if (
            await session.execute(
                select(TodoDatabase.User).where(TodoDatabase.User.id == user_id)
            )
        ).first() is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
            )

        session.add(
            TodoDatabase.Todo(id=str(uuid1()), **body.model_dump(), user_id=user_id)
        )

        await session.commit()
        return "Successfully created"
