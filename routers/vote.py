"""The router file for the vote"""
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session

from db.database import get_db
from models.models import Votes
from schemas.vote_schemas import Vote
from oauth2 import get_current_user

vote_router = APIRouter(prefix='/vote', tags=['votes'])


@vote_router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(
    _vote: Vote,
    _db: Session = Depends(get_db),
    _current_user=Depends(get_current_user)
):
    _vote_query = _db.query(Votes).filter(
        Votes.post_id == _vote.post_id, Votes.user_id == _current_user.id)
    _found_vote = _vote_query.first()

    if _found_vote:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"user {_current_user.id} has already voted on the post with an id of {_vote.post_id}"
        )
