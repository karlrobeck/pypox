from user.schemas import User


async def endpoint(body: User) -> str:
    return body.name
