"""The file that contains the votes schema"""
from typing import Optional

from pydantic import BaseModel, conint


class Vote(BaseModel):
    post_id: int
    direction: Optional[conint(le=1)]
