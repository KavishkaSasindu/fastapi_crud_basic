from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title="Monolithic-App",
    lifespan=lifespan
)


