from test.app.database.models import Todo
from test.app.database.session import AsyncSession, dbSession
from test.app.routes.todo.schemas import UserTodo
from sqlmodel import select
from fastapi import Depends, HTTPException, status


async def endpoint(user_id: str, id: str, db: AsyncSession = Depends(dbSession)):
    """
    delete a todo
    """

    # find todo in the database
    todo = (
        (await db.execute(select(Todo).where(Todo.id == id, Todo.user_id == user_id)))
        .scalars()
        .first()
    )

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="todo not found"
        )
    # delete the todo in the database
    await db.delete(todo)
    await db.commit()

    return "Successfully deleted"
