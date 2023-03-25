"""The main file for the project"""
from fastapi import FastAPI

from models import models
from routers.users import users_router
from routers.posts import posts_router
from db.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: Returns a message to show successful execution
    """
    return {"message": "The api works"}

app.include_router(users_router)
app.include_router(posts_router)
