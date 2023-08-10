import os
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.pool import NullPool

load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']
print("DATABASE URL: ", DATABASE_URL)

engine = create_async_engine(DATABASE_URL, poolclass=NullPool,
                             connect_args={})

Base = declarative_base()

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session