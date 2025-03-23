from models.user_model import UserModel
from db.sqllite_client import SqLiteClient
from typing import Tuple, Optional, List, Dict, Any
from repositories.meta.interface_user_repository import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.db_client = SqLiteClient()
    
    def create(self, first_name: str, email: str, last_name: str = None) -> Tuple[UserModel, Optional[str], Optional[str]]:
        with next(self.db_client()) as db_session:
            user = UserModel(first_name=first_name,
                            last_name=last_name,
                            email=email)
            db_session.add(user)
            db_session.commit()
            db_session.refresh(user) 
            return (user, None, "")
    
    def select_all(self) -> Tuple[List[UserModel], Optional[str], Optional[str]]:
        with next(self.db_client()) as db_session:
            users = db_session.query(UserModel).all()
            return (users, None, "")
    
    def select_by_id(self, user_id: int) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        with next(self.db_client()) as db_session:
            user = db_session.query(UserModel).filter(UserModel.id == user_id).first()
            if not user:
                return (None, "UserNotExists", f"User with id {user_id} not exists.")
            return (user, None, "")

    def update(self, user_id: int, first_name: str, email: str, last_name: str = None) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        with next(self.db_client()) as db_session:
            user = self.select_by_id(user_id)[0]
            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                db_session.commit()
                db_session.close()
                return (user, None, "")
            else:
                return (None, "UserNotExists", f"User with id {user_id} not exists.")

    def delete_by_id(self, user_id) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        with next(self.db_client()) as db_session:
            user = self.select_by_id(user_id)[0]
            if not user:
                return (None, "UserNotExists", f"User with id {user_id} not exists.")
            
            db_session.delete(user)
            db_session.commit()
            return (user, None, "")

if __name__ == "__main__":
    repo = UserRepository()

    tuple_response = repo.create("João", "Silva", "joao@email.com")
    print("Usuário criado:", {tuple_response[0].__dict__})

    user_id = tuple_response[0].__dict__["id"]
    tuple_response = repo.select_by_id(user_id)
    print("Usuário encontrado:", tuple_response[0].__dict__)

    print("Lista de usuários:", repo.select_all())

    tuple_response = repo.update(user_id, "João", "Santos", "joao_santos@email.com")
    print("Usuário atualizado:", tuple_response[0].__dict__)

    tuple_response = repo.delete_by_id(user_id)
    print("Usuário removido:", tuple_response[0].__dict__) 