from abc import ABC, abstractmethod
from typing import Tuple, Optional, List
from models.user_model import UserModel


class IUserRepository(ABC):
    @abstractmethod
    def create(self, first_name, email, last_name=None) -> Tuple[UserModel, Optional[str], Optional[str]]:
        pass
    
    @abstractmethod
    def select_all(self) -> Tuple[List[UserModel], Optional[str], Optional[str]]:
        pass

    @abstractmethod
    def select_by_id(self, user_id: int) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        pass

    @abstractmethod
    def update(self, user_id: int, first_name: str, email: str, last_name: str = None) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        pass

    @abstractmethod
    def delete_by_id(self, user_id: int) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        pass