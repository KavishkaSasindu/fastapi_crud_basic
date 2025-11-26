from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import config

DB_URL = f"mysql+aiomysql://{config.DB_USER}:{config.ENCODE_PASS}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

asycn_engine = create_async_engine(
    DB_URL,
    echo=True,
    pool_pre_ping=True
)

AsyncSessionLocal = async_sessionmaker(
    bind=asycn_engine,
    autoflush=False,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass