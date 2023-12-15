from sqlalchemy import Row
from test.app.database.models import User
from test.app.database.session import AsyncSession, dbSession
from fastapi import status, Depends, HTTPException
from sqlmodel import select
from test.app.routes.auth.login.schemas import UserLogin


async def endpoint(body: UserLogin, db: AsyncSession = Depends(dbSession)):
    """
    login the user
    """
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
