import asyncio
import os
from types import ModuleType
from typing import Any, Optional
from sqlalchemy import Engine
from sqlmodel import create_engine as alchemy_create_engine
from sqlalchemy.ext.asyncio import (
    create_async_engine as alchemy_create_engine_async,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.orm import Session
from contextvars import ContextVar

engines_sync: ContextVar[dict[str, Engine]] = ContextVar("engines_sync")
engines_async: ContextVar[dict[str, AsyncEngine]] = ContextVar("engines_async")


def create_engine_sync(module, **kwargs):
    # get the name
    db_name = module.__name__.split(".")[-1].lower()
    dialect = module.__name__.split(".")[-2].lower()
    db_path = (
        os.path.dirname(module.__file__).replace(os.getcwd(), "").replace("\\", "/")
    )
    # connect to database
    engine = alchemy_create_engine(f"{dialect}://{db_path}/{db_name}.db", **kwargs)
    return engine


def create_engine_async(module, driver, **kwargs) -> AsyncEngine:  # type: ignore
    db_name = module.__name__.split(".")[-1].lower()
    dialect = module.__name__.split(".")[-2].lower()
    db_path = (
        os.path.dirname(module.__file__).replace(os.getcwd(), "").replace("\\", "/")
    )
    if dialect == "sqlite":
        print("sqlite")
        return alchemy_create_engine_async(
            f"{dialect}+{driver}://{db_path}/{db_name}.db", **kwargs
        )


def init_database_sync(engine, module):
    # initialize database
    module.SQLModel.metadata.create_all(engine)


async def init_database_async(engine: AsyncEngine, module: Any) -> None:
    """
    Initialize the database asynchronously.

    Args:
        engine (Engine): The SQLAlchemy engine instance.
        module (Any): The module containing the SQLModel metadata.
    """
    async with engine.begin() as connection:
        await connection.run_sync(module.SQLModel.metadata.create_all)


def createSyncEngine(module: ModuleType, **kwargs):
    """
    create new engine and add it to context var
    """

    engine = create_engine_sync(module, **kwargs)

    engines_dict: dict[str, Engine] = engines_sync.get({})

    engines_dict[module.__name__.split(".")[-1].lower()] = engine

    engines_sync.set(engines_dict)
    return


def createAsyncEngine(module: ModuleType, driver: str, **kwargs):
    """
    create new engine and add it to context var
    """

    engine = create_engine_async(module, driver, **kwargs)

    engines_dict: dict[str, AsyncEngine] = engines_async.get({})

    engines_dict[module.__name__.split(".")[-1].lower()] = engine

    engines_async.set(engines_dict)
    return


def getSyncEngine(database: ModuleType | str) -> Engine:
    if isinstance(database, str):
        engine: Engine = engines_sync.get()[database.lower()]
    elif isinstance(database, ModuleType):
        engine: Engine = engines_sync.get()[database.__name__.split(".")[-1].lower()]
    return engine


def getAsyncEngine(database: ModuleType | str) -> AsyncEngine:
    if isinstance(database, str):
        engine: AsyncEngine = engines_async.get()[database.lower()]
    elif isinstance(database, ModuleType):
        engine: AsyncEngine = engines_async.get()[
            database.__name__.split(".")[-1].lower()
        ]
    return engine


async def asyncDbSession(database: ModuleType | str) -> AsyncSession:
    # get the engine
    if isinstance(database, str):
        engine: AsyncEngine = getAsyncEngine(database)
    elif isinstance(database, ModuleType):
        engine: AsyncEngine = getAsyncEngine(database.__name__.split(".")[-1].lower())
    return AsyncSession(engine)


def syncDbSession(database: ModuleType | str) -> Session:
    # get the engine
    if isinstance(database, str):
        engine: Engine = getSyncEngine(database)
    elif isinstance(database, ModuleType):
        engine: Engine = getSyncEngine(database.__name__.split(".")[-1].lower())

    return Session(engine)


"""
if __name__ == "__main__":
    new_engine_sync: Engine = create_engine_sync(TodoDatabase)
    new_engine_async: AsyncEngine = create_engine_async(TodoDatabase, "aiosqlite")
    asyncio.run(init_database_async(new_engine_async, TodoDatabase))
"""
