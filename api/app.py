from fastapi import FastAPI
from controller.user_controller import UserController

app = FastAPI()

app.include_router(UserController.router, prefix="/api", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI CRUD API"}