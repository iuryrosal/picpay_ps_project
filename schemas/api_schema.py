from pydantic import BaseModel
from typing import List, Optional


class GenericOkResponse(BaseModel):
    code: str
    msg: str
    data: List = []

class GenericErrorResponse(BaseModel):
    status: str
    code: str
    msg: str
    detail: Optional[str]