from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
import ssl
from app.core.config import DATABASE_URL

ssl_context = ssl._create_unverified_context()

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"ssl": ssl_context},
)

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Base = declarative_base()


async def get_db():
    async with SessionLocal() as session:
        yield session