from uuid import uuid1
from fastapi import Depends, HTTPException, status
from test.app.database.models import User
from test.app.database.session import dbSession, AsyncSession
from test.app.routes.auth.register.schemas import UserRegister
from sqlmodel import select


async def endpoint(body: UserRegister, db: AsyncSession = Depends(dbSession)):
    # check if user exist

    if (await db.execute(select(User).where(User.username == body.username))).first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="user already exist"
        )

    db.add(User(id=str(uuid1()), **body.model_dump()))

    # check user if exist in the database

    # create user in the database
    return "Successfully registered"
