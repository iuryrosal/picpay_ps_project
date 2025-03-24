from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreateRequest(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr


class UserUpdateRequest(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None


class UserGeneralResponse(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    email: EmailStr
