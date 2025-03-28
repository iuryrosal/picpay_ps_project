import http
from fastapi import APIRouter, Depends
from typing import List, Tuple
from schemas.user_schema import UserCreateRequest, UserGeneralResponse, UserUpdateRequest
from schemas.api_schema import GenericErrorResponse, GenericOkResponse
from fastapi.responses import JSONResponse
from models.user_model import UserModel
from service.meta.interface_user_service import IUserService
from service.user_service import UserService
from repositories.sqlite_user_repository import SQLiteUserRepository


def get_user_service() -> IUserService:
    user_repo = SQLiteUserRepository()
    return UserService(user_repo)


class UserController:
    """Controller que estabelecerá as rotas e lógicas de validação da API no contexto de usuários (User).
    
    Após validada, utilizará a camada service para estabelecer lógicas de negócio e, posteriormente, comunicação com a camada repositório.
    """
    router = APIRouter()

    def __verify_error_tuple(error_tuple:  Tuple[str, str]):
        def is_tuple(obj):
            return isinstance(obj, tuple)
        
        def is_tuple_with_2_items(obj):
            return len(obj) == 2
        
        def is_tuple_only_str(obj):
            return all(isinstance(item, str) for item in error_tuple)

        if not is_tuple(error_tuple):
            raise Exception(f"Service error tuple response have invalid format: {type(error_tuple)}")
        elif not is_tuple_with_2_items(error_tuple) and is_tuple_only_str(error_tuple):
            raise Exception(f"Service error tuple response have invalid values: {error_tuple}")

    def __handle_error_response_from_service(error_tuple:  Tuple[str, str]):
        """Em caso de falha detectada durante processamento da requisição, irá processar a tupla de erros (Título (str), Descrição (str)) gerando uma exceção em caso de tupla inválida e, em caso válido, gerará uma response padronizada de erro (JsonResponse).

        Args:
            error_tuple (Tuple[str, str]): _description_

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            JSONResponse: Padrão de resposta de requisição com status_code do HTTP e conteúdo no padrão do schema GenericErrorResponse, contendo status por texto, código do erro (título do erro), mensagem com a descrição do erro e detalhes.
        """
        UserController.__verify_error_tuple(error_tuple)

        if error_tuple[0] == "UserDoesNotExist":
            http_status_obj = http.HTTPStatus.NOT_FOUND
            response = GenericErrorResponse(
                status=http_status_obj.phrase,
                code=error_tuple[0],
                msg=error_tuple[1],
                detail=None
            )
            return JSONResponse(status_code=http_status_obj,
                                content=response.dict())
        elif error_tuple[0] == "UnexpectedError":
            http_status_obj = http.HTTPStatus.INTERNAL_SERVER_ERROR
            response = GenericErrorResponse(
                status=http_status_obj.phrase,
                code=error_tuple[0],
                msg=error_tuple[1],
                detail=None
            )
            return JSONResponse(status_code=http_status_obj,
                                content=response.dict())
        else:
            http_status_obj = http.HTTPStatus.BAD_REQUEST
            response = GenericErrorResponse(
                status=http_status_obj.phrase,
                code=error_tuple[0],
                msg=error_tuple[1],
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
            return UserController.__handle_error_response_from_service(response)

    @router.get("/users/", status_code=200, response_model=List[UserGeneralResponse])
    async def get_users(service: IUserService = Depends(get_user_service)):
        response = service.get_all_users()
        if isinstance(response, list) and all(isinstance(item, UserModel) for item in response):
            return response
        else:
            return UserController.__handle_error_response_from_service(response)


    @router.get("/users/{user_id}", status_code=200, response_model=UserGeneralResponse)
    async def get_user(user_id: int, service: IUserService = Depends(get_user_service)):
        response = service.get_user(user_id=user_id)
        if isinstance(response, UserModel):
            return response
        else:
            return UserController.__handle_error_response_from_service(response)


    @router.put("/users/{user_id}", status_code=200, response_model=UserGeneralResponse)
    async def update_user(user_id: int, user_update: UserUpdateRequest, service: IUserService = Depends(get_user_service)):
        response = service.update_user(user_id, user_update.dict())
        if isinstance(response, UserModel):
            return response
        else:
            return UserController.__handle_error_response_from_service(response)


    @router.delete("/users/{user_id}", status_code=200, response_model=GenericOkResponse)
    async def delete_user(user_id: int, service: IUserService = Depends(get_user_service)):
        response = service.delete_user(user_id)
        if isinstance(response, UserModel):
            generic_response = GenericOkResponse(
                code="UserDeleted",
                msg=f"Usuário com id {response.id} deletado com sucesso."
            )
            return JSONResponse(status_code=http.HTTPStatus.OK,
                                content=generic_response.dict())
        else:
            return UserController.__handle_error_response_from_service(response)