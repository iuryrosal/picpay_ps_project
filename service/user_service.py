from typing import List, Union
from repositories.meta.interface_user_repository import IUserRepository
from models.user_model import UserModel
from service.meta.interface_user_service import IUserService


class UserService(IUserService):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def create_user(self, first_name: str, last_name: str, email: str) -> Union[UserModel, str]:
        user, error_type, error_msg = self.repository.create(first_name, last_name, email)
        if user:
            return user
        else:
            return f"{error_type}: {error_msg}"

    def get_user(self, user_id: int) -> Union[UserModel, str]:
        user, error_type, error_msg = self.repository.select_by_id(user_id)
        if user:
            return user
        else:
            return f"{error_type}: {error_msg}"

    def get_all_users(self) -> Union[List[UserModel], str]:
        users, error_type, error_msg  = self.repository.select_all()
        if users:
            return users
        else:
            return f"{error_type}: {error_msg}"

    def update_user(self, user_id: int, first_name: str, last_name: str, email: str) -> Union[UserModel, str]:
        user, error_type, error_msg  = self.repository.update(user_id, first_name, last_name, email)
        if user:
            return user
        else:
            return f"{error_type}: {error_msg}"

    def delete_user(self, user_id: int) -> Union[UserModel, str]:
        user, error_type, error_msg  = self.repository.delete_by_id(user_id)
        if user:
            return user
        else:
            return f"{error_type}: {error_msg}"