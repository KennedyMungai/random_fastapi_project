"""The main file for the project"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "The api works"}
