from typing import AsyncGenerator
from sqlalchemy import Row
from fastapi import status, Depends, HTTPException
from sqlmodel import select
from test.app.database.SQLITE.TodoDatabase import User, Todo
from test.app.routes.auth.login.schemas import UserLogin
from test.app.startup import dbSession, AsyncSession


async def endpoint(body: UserLogin):
    """
    login the user
    """
    db: AsyncSession = await dbSession()
    # check if the user exist in the database
    user: Row[tuple[User]] | None = (
        await db.execute(select(User).where(User.username == body.username))
    ).one()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect username or password",
        )

    return user[0].id
