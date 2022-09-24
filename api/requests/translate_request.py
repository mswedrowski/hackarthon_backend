from typing import Union
from pydantic import BaseModel


class TranslateRequest(BaseModel):
    text: str