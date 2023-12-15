from .models import async_engine
from sqlalchemy.ext.asyncio import AsyncSession


async def dbSession():
    async with AsyncSession(async_engine) as session:
        async with session.begin():
            yield session
