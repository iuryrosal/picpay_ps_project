from pydantic import BaseModel

from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: str
    first_name: str
    last_name: Optional[str]
    email: str
    created_at: datetime
    updated_at: Optional[datetime]