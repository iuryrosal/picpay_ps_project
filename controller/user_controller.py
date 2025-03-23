import http
from fastapi import APIRouter, Depends
from typing import List, Tuple
from schemas.user_schema import UserCreateRequest, UserGeneralResponse, UserUpdateRequest
from schemas.api_schema import GenericErrorResponse, GenericOkResponse
from fastapi.responses import JSONResponse
from models.user_model import UserModel
from service.meta.interface_user_service import IUserService
from service.user_service import UserService
from repositories.user_repository import UserRepository


def get_user_service() -> IUserService:
    user_repo = UserRepository()
    return UserService(user_repo)


class UserController:
    router = APIRouter()

    def _handle_error_response_from_service(error_tuple:  Tuple[str, str]):
        if not isinstance(error_tuple, tuple) and len(error_tuple) == 2 and all(isinstance(item, str) for item in error_tuple):
            raise Exception(f"Service error tuple response have invalid format: {type(error_tuple)}")
        elif not len(error_tuple) == 2 and not all(isinstance(item, str) for item in error_tuple):
            raise Exception(f"Service error tuple response have invalid values: {error_tuple}")

        if error_tuple[0] == "UserNotExists":
            http_status_obj = http.HTTPStatus.NOT_FOUND
            response = GenericErrorResponse(
                status=http_status_obj.phrase,
                code=error_tuple[0],
                title=error_tuple[1],
                detail=None
            )
            return JSONResponse(status_code=http_status_obj,
                                content=response.dict())
        else:
            http_status_obj = http.HTTPStatus.BAD_REQUEST
            response = GenericErrorResponse(
                status=http_status_obj.phrase,
                code=error_tuple[0],
                title=error_tuple[1],
                detail=None
            )
            return JSONResponse(status_code=http_status_obj,
                                content=response.dict())

    @router.post("/users/", status_code=201, response_model=UserGeneralResponse)
    async def create_user(user: UserCreateRequest, service: IUserService = Depends(get_user_service)):
        response = service.create_user(**user.dict())
        if isinstance(response, UserModel):
            return response
        else:
            return UserController._handle_error_response_from_service(response)

    @router.get("/users/", status_code=200, response_model=List[UserGeneralResponse])
    async def get_users(service: IUserService = Depends(get_user_service)):
        response = service.get_all_users()
        if isinstance(response, list) and all(isinstance(item, UserModel) for item in response):
            return response
        else:
            return UserController._handle_error_response_from_service(response)


    @router.get("/users/{user_id}", status_code=200, response_model=UserGeneralResponse)
    async def get_user(user_id: int, service: IUserService = Depends(get_user_service)):
        response = service.get_user(user_id=user_id)
        if isinstance(response, UserModel):
            return response
        else:
            return UserController._handle_error_response_from_service(response)


    @router.put("/users/{user_id}", status_code=200, response_model=UserGeneralResponse)
    async def update_user(user_id: int, user_update: UserUpdateRequest, service: IUserService = Depends(get_user_service)):
        response = service.update_user(user_id, user_update.dict())
        if isinstance(response, UserModel):
            return response
        else:
            return UserController._handle_error_response_from_service(response)


    @router.delete("/users/{user_id}", status_code=200, response_model=GenericOkResponse)
    def delete_user(user_id: int, service: IUserService = Depends(get_user_service)):
        response = service.delete_user(user_id)
        if isinstance(response, UserModel):
            generic_response = GenericOkResponse(
                title="Usuário Deletado.",
                message=f"Usuário com id {response.id} deletado com sucesso."
            )
            return JSONResponse(status_code=http.HTTPStatus.CREATED,
                                content=generic_response.dict())
        else:
            return UserController._handle_error_response_from_service(response)