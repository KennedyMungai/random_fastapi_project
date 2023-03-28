"""The router file for the vote"""
from fastapi import APIRouter, status, Depends
from schemas.vote_schemas import Vote
from db.database import get_db
from sqlalchemy.orm.session import Session
from oauth2 import get_current_user


vote_router = APIRouter(prefix='/vote', tags=['votes'])


@vote_router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(
    _vote: Vote,
    _db: Session = Depends(get_db),
    _current_user=Depends(get_current_user)
):
    pass
