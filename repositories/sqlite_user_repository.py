from models.user_model import UserModel
from db.sqllite_client import SqLiteClient
from typing import Tuple, Optional, List
from repositories.meta.interface_user_repository import IUserRepository


class SQLiteUserRepository(IUserRepository):
    """
        Realiza implementação da interface do repositório de usuário (IUserRepository), que irá estabelecer conexão com o banco de dados SQLite (utilizando o SQLiteClient) e, por meio de ORM, realizar as operações necessárias.
    """

    _instance = None
    def __new__(cls, *args, **kwargs): # Singleton
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.db_client = SqLiteClient()
    
    def create(self, first_name: str, email: str, last_name: str = None) -> Tuple[UserModel, Optional[str], Optional[str]]:
        with self.db_client._get_session() as db_session:
            user = UserModel(first_name=first_name,
                            last_name=last_name,
                            email=email)
            db_session.add(user)
            db_session.commit()
            db_session.refresh(user) 
            return (user, None, None)
    
    def select_all(self) -> Tuple[List[UserModel], Optional[str], Optional[str]]:
        with self.db_client._get_session() as db_session:
            users = db_session.query(UserModel).all()
            return (users, None, None)
    
    def select_by_id(self, user_id: int) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        with self.db_client._get_session() as db_session:
            user = db_session.query(UserModel).filter(UserModel.id == user_id).first()
            if not user:
                return (None, "UserDoesNotExist", f"User with id {user_id} does not exist.")
            return (user, None, None)

    def update(self, user_id: int, new_user_data: dict) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        with self.db_client._get_session() as db_session:
            result = db_session.query(UserModel).filter(UserModel.id == user_id).update(
                {key: value for key, value in new_user_data.items() if value is not None}
            )

            if not result:
                return (None, "UserDoesNotExist", f"User with id {user_id} does not exist.")

            db_session.commit()

            user = db_session.query(UserModel).filter(UserModel.id == user_id).first()
            return (user, None, None)

    def delete_by_id(self, user_id) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        with self.db_client._get_session() as db_session:
            user = db_session.query(UserModel).filter(UserModel.id == user_id).first()
            if not user:
                return (None, "UserDoesNotExist", f"User with id {user_id} does not exist.")
            
            db_session.delete(user)
            db_session.commit()
            return (user, None, None)