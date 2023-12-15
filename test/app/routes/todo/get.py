from test.app.database.models import Todo
from test.app.database.session import AsyncSession, dbSession
from test.app.routes.todo.schemas import UserTodo, UserTodoWithId
from fastapi import status, Depends, HTTPException
from sqlmodel import select


async def endpoint(user_id: str, db: AsyncSession = Depends(dbSession)):
    try:
        todo = await db.execute(select(Todo).where(Todo.user_id == user_id))
        return [UserTodoWithId(**x.model_dump()) for x in todo.scalars().all()]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="todo not found"
        )
