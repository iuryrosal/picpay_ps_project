from fastapi import APIRouter, HTTPException
from typing import List, Tuple, Union
from schemas.user_schema import UserCreateRequest, UserGeneralResponse, UserUpdateRequest
from models.user_model import UserModel
from service.meta.interface_user_service import IUserService


class UserController:
    router = APIRouter()

    def _handle_response_from_service(response: Union[UserModel, List[UserModel], Tuple[str, str]], object_expected: Union[UserModel, list]):
        if isinstance(response, object_expected):
            return response
        elif isinstance(response, str):
            if response[0] == "UserNotExists":
                raise HTTPException(status_code=404, detail=f"{response[0]}: {response[1]}")
            else:
                raise HTTPException(status_code=400, detail=f"{response[0]}: {response[1]}")
        else:
            raise Exception(f"Service response have invalid format: {type(response)}")

    @router.post("/users/", status_code=201, response_model=UserGeneralResponse)
    def create_customer(user: UserCreateRequest, service: IUserService):
        response = service.create_user(**user.dict())
        return UserController._handle_response_from_service(response, object_expected=UserModel)

    @router.get("/users/", status_code=200, response_model=List[UserGeneralResponse])
    def get_customers(service: IUserService):
        response = service.get_all_users()
        return UserController._handle_response_from_service(response, object_expected=list)


    @router.get("/users/{user_id}", status_code=200, response_model=UserGeneralResponse)
    def get_customer(user_id: int, service: IUserService):
        response = service.get_user(user_id=user_id)
        return UserController._handle_response_from_service(response, object_expected=UserModel)


    @router.put("/users/{user_id}", status_code=200, response_model=UserGeneralResponse)
    def update_customer(user_id: int, user_update: UserUpdateRequest, service: IUserService):
        response = service.update_user(user_id, **user_update.dict())
        return UserController._handle_response_from_service(response, object_expected=UserModel)


    @router.delete("/users/{user_id}")
    def delete_customer(user_id: int, service: IUserService):
        response = service.delete_user(user_id)
        return UserController._handle_response_from_service(response, object_expected=UserModel)