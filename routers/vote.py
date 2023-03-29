"""The router file for the vote"""
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm.session import Session

from db.database import get_db
from models.models import Votes, Post
from schemas.vote_schemas import Vote
from oauth2 import get_current_user

vote_router = APIRouter(prefix='/vote', tags=['votes'])


@vote_router.post("/", status_code=status.HTTP_201_CREATED)
async def vote(
    _vote: Vote,
    _db: Session = Depends(get_db),
    _current_user=Depends(get_current_user)
):
    """The vote endpoint

    Args:
        _vote (Vote): The vote template
        _db (Session, optional): The database session.
                                Defaults to Depends(get_db).
        _current_user (_type_, optional): The user currently logged in.
                                Defaults to Depends(get_current_user).

    Raises:
        HTTPException: _description_
    """
    post = _db.query(Post).filter(Post.id == _vote.post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The post with id: {Post.id} does not exist"
        )

    _vote_query = _db.query(Votes).filter(
        Votes.post_id == _vote.post_id, Votes.user_id == _current_user.id)
    _found_vote = _vote_query.first()

    if _vote.direction == 1:
        if _found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user {_current_user.id} has already voted on the post with an id of {_vote.post_id}"
            )

        _new_vote = Votes(post_id=_vote.post_id, user_id=_current_user.id)
        _db.add(_new_vote)
        _db.commit()

        return {"message": "Successfully added a vote"}

    else:
        if not _found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Vote does not exist"
            )

        _vote_query.delete()
        _db.commit()
