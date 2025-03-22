from pydantic import BaseModel, EmailStr

from typing import Optional
from datetime import datetime


class UserSchema(BaseModel):
    id: str
    first_name: str
    last_name: Optional[str]
    email: EmailStr
    created_at: datetime
    updated_at: Optional[datetime]