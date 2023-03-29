"""The main file for the project"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.auth import login_router
from routers.posts import posts_router
from routers.users import users_router
from routers.vote import vote_router

app = FastAPI()

origins = [
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost",
    "https://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


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
