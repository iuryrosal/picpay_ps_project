from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreateRequest(BaseModel):
    first_name: str
    last_name: Optional[str]
    email: EmailStr


class UserUpdateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]


class UserGeneralResponse(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    email: EmailStr
