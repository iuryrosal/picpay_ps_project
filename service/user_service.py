from typing import List, Union, Tuple
from repositories.meta.interface_user_repository import IUserRepository
from models.user_model import UserModel
from service.meta.interface_user_service import IUserService


class UserService(IUserService):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def _handle_response_from_repository(self,
                                         object_expected: Union[UserModel, List[UserModel], None],
                                         error_type: Union[str, None],
                                         error_msg: Union[str, None]) -> Union[UserModel, List[UserModel], Tuple[str, str]]:
        if object_expected:
            return object_expected
        else:
            return (error_type, error_msg)

    def create_user(self, first_name: str, email: str, last_name: str = None) -> Union[UserModel, Tuple[str, str]]:
        user, error_type, error_msg = self.repository.create(first_name=first_name,
                                                             last_name=last_name,
                                                             email=email)
        return self._handle_response_from_repository(user, error_type, error_msg)

    def get_user(self, user_id: int) -> Union[UserModel, Tuple[str, str]]:
        user, error_type, error_msg = self.repository.select_by_id(user_id)
        return self._handle_response_from_repository(user, error_type, error_msg)

    def get_all_users(self) -> Union[List[UserModel], Tuple[str, str]]:
        users, error_type, error_msg  = self.repository.select_all()
        return self._handle_response_from_repository(users, error_type, error_msg)

    def update_user(self, user_id: int, first_name: str, last_name: str, email: str) -> Union[UserModel, Tuple[str, str]]:
        user, error_type, error_msg  = self.repository.update(user_id, first_name, last_name, email)
        return self._handle_response_from_repository(user, error_type, error_msg)

    def delete_user(self, user_id: int) -> Union[UserModel, Tuple[str, str]]:
        user, error_type, error_msg  = self.repository.delete_by_id(user_id)
        return self._handle_response_from_repository(user, error_type, error_msg)

