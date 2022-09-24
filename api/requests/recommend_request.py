from typing import Union
from pydantic import BaseModel


class RecommendEventRequest(BaseModel):
    username: str