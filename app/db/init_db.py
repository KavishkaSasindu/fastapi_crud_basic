from app.db.base import Base
from app.db.session import asycn_engine

async def init_db():
    async with asycn_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)