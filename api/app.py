from fastapi import APIRouter
from api.v1 import user

api_router = APIRouter(prefix="/v1")
api_router.include_router(user.router)