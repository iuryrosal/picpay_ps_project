from ..models.user import UserModel
from ..db.sqllite_client import SqLiteClient
from typing import Dict, Any


class UserRepository:
    def __init__(self) -> None:
        self.db_client = SqLiteClient()
    
    def create_user(self, id, first_name, email, last_name=None):
        user = UserModel(id=id,
                         first_name=first_name,
                         last_name=last_name,
                         email=email)
        self.db_client().add(user)
        self.db_client().commit()
    
    def select_all_users(self):
        return self.db_client().query(UserModel).all()
    
    def select_user_by_id(self, user_id):
        return self.db_client().query(UserModel).filter(UserModel.id == user_id).first()

    def update(self, data: Dict[str, Any]):
        for key, value in data.items():
            if hasattr(UserModel, key):
                setattr(UserModel, key, value)
            else:
                raise AttributeError(f"{type(UserModel).__name__} has no attribute '{key}'")

        self.db_client().commit()

    def delete_user_by_id(self, user_id) -> None:
        user = self.select_user_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not exists.")
        
        self.db_client().delete(user)
        self.db_client().commit()