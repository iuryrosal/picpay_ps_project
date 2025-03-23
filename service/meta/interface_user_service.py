from typing import List, Union
from models.user_model import UserModel
from abc import ABC, abstractmethod


class IUserService(ABC):
    @abstractmethod
    def create_user(self, first_name: str, last_name: str, email: str) -> Union[UserModel, str]:
        pass
    
    @abstractmethod
    def get_user(self, user_id: int) -> Union[UserModel, str]:
        pass
    
    @abstractmethod
    def get_all_users(self) -> Union[List[UserModel], str]:
        pass

    @abstractmethod
    def update_user(self, user_id: int, first_name: str, last_name: str, email: str) -> Union[UserModel, str]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> Union[UserModel, str]:
        pass