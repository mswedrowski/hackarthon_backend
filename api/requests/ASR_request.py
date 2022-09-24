from typing import Union
from pydantic import BaseModel


class ASRRequest(BaseModel):
    url: str