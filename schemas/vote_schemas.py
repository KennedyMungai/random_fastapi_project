"""The file that contains the votes schema"""
from typing import Optional

from pydantic import BaseModel, conint


class Vote(BaseModel):
    """The vote schema class

    Args:
        BaseModel (Class): The parent class
    """
    post_id: int
    direction: Optional[conint(le=1)]
