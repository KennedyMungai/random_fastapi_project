"""The main file for the project"""
from fastapi import FastAPI

from db.database import engine
from models import models
from routers.auth import login_router
from routers.posts import posts_router
from routers.users import users_router
from routers.vote import vote_router

app = FastAPI()


@app.get("/", tags=["Root"])
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: Returns a message to show successful execution
    """
    return {"message": "The api works"}

app.include_router(users_router)
app.include_router(posts_router)
app.include_router(login_router)
app.include_router(vote_router)
