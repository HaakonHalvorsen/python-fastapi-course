from contextlib import asynccontextmanager

from fastapi import FastAPI

from socialmedia_api.database import database
from socialmedia_api.routers.post import router as post_router


# Context manager: Does setup and tear down
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()  # When app is starting
    yield  # Stops running until FastAPI tells it to continue
    await database.disconnect()  # When app tears down


app = FastAPI(lifespan=lifespan)


app.include_router(post_router)
