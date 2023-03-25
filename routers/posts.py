"""The file contains the information on the posts route"""
from fastapi import APIRouter

posts_router = APIRouter(prefix="/posts", tags=["Posts"])
