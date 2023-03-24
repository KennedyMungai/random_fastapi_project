"""The main file for the project"""
from fastapi import Body, FastAPI


app = FastAPI()


@app.get("/")
async def root() -> dict:
    """The root api endpoint

    Returns:
        dict: Returns a message to show successful execution
    """
    return {"message": "The api works"}


@app.post("/createposts")
async def create_posts(payload: dict = Body(...)) -> dict:
    """A dummy post creator endpoint

    Returns:
        dict: A message to show successful code execution
    """
    return {"new post": payload}
