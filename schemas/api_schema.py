from pydantic import BaseModel
from typing import List, Optional


class GenericOkResponse(BaseModel):
    title: str
    message: str

class GenericErrorResponse(BaseModel):
    status: str
    code: str
    title: str
    detail: Optional[str]