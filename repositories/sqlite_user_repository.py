from models.user_model import UserModel
from db.sqllite_client import SqLiteClient
from typing import Tuple, Optional, List
from repositories.meta.interface_user_repository import IUserRepository


class SQLiteUserRepository(IUserRepository):
    """Realiza implementação da interface do repositório de usuário (IUserRepository), que irá estabelecer conexão com o banco de dados SQLite (utilizando o SQLiteClient) e, por meio de ORM, realizar as operações necessárias.
    """
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

    def update(self, user_id: int, new_user_data: dict) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        with next(self.db_client()) as db_session:
            user = db_session.query(UserModel).filter(UserModel.id == user_id).first()
            if not user:
                return (None, "UserNotExists", f"User with id {user_id} not exists.")

            for key, value in new_user_data.items():
                if value is not None:
                    setattr(user, key, value)

            db_session.commit()
            db_session.refresh(user)
            db_session.close()
            return (user, None, "")

    def delete_by_id(self, user_id) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        with next(self.db_client()) as db_session:
            user = db_session.query(UserModel).filter(UserModel.id == user_id).first()
            if not user:
                return (None, "UserNotExists", f"User with id {user_id} not exists.")
            
            db_session.delete(user)
            db_session.commit()
            return (user, None, "")

if __name__ == "__main__":
    repo = SQLiteUserRepository()

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