from uuid import uuid1
from fastapi import Depends, HTTPException, status
from test.app.database.SQLITE.TodoDatabase import User, Todo
from test.app.startup import dbSession, AsyncSession
from test.app.routes.auth.register.schemas import UserRegister
from sqlmodel import select


async def endpoint(
    body: UserRegister,
):
    # check if user exist
    db: AsyncSession = await dbSession()
    if (await db.execute(select(User).where(User.username == body.username))).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="user already exist"
        )

    db.add(User(id=str(uuid1()), **body.model_dump()))

    # check user if exist in the database

    # create user in the database
    return "Successfully registered"
