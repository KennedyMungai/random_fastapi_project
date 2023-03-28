"""The router file for the vote"""
from fastapi import APIRouter


vote_router = APIRouter(prefix='/vote', tags=['votes'])
