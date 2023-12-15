from test.app.database.models import Todo
from test.app.database.session import dbSession, AsyncSession
from test.app.routes.todo.schemas import UserTodo
from sqlmodel import select
from fastapi import Depends, status, HTTPException


async def endpoint(
    user_id: str, id: str, body: UserTodo, db: AsyncSession = Depends(dbSession)
):
    # find todo in the database
    todo = (
        await db.execute(select(Todo).where(Todo.id == id, Todo.user_id == user_id))
    ).one()

    # update the todo in the database
    todo[0].title = body.title or todo[0].title
    todo[0].description = body.description or todo[0].description
    todo[0].completed = body.completed

    db.add(todo[0])
    await db.commit()

    return "Successfully updated"
