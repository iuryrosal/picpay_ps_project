from fastapi import FastAPI
from controller.v1.user_controller import UserController

app = FastAPI()

app.include_router(UserController.router, prefix="/api/v1", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CRUD API"}