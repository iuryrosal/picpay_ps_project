from models.user_model import UserModel
from db.sqllite_client import SqLiteClient
from typing import Tuple, Optional, List
from repositories.meta.interface_user_repository import IUserRepository


class SQLiteUserRepository(IUserRepository):
    """Realiza implementação da interface do repositório de usuário, que irá estabelecer conexão com o banco de dados SQLite (utilizando o SQLiteClient) e, por meio de ORM, realizar as operações necessárias.
    """
    def __init__(self) -> None:
        self.db_client = SqLiteClient()
    
    def create(self, first_name: str, email: str, last_name: str = None) -> Tuple[UserModel, Optional[str], Optional[str]]:
        """Realiza criação de um usuário no banco de dados, sendo necessário a adição automática de id com lógica incremental para cada usuário criado.

        Args:
            first_name (str): Primeiro nome do usuário
            email (str): Email atrelado ao usuário
            last_name (str, optional): Sobrenome do usuário. Padrão para None.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá o objeto usuário criado (UserModel), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
        with next(self.db_client()) as db_session:
            user = UserModel(first_name=first_name,
                            last_name=last_name,
                            email=email)
            db_session.add(user)
            db_session.commit()
            db_session.refresh(user) 
            return (user, None, "")
    
    def select_all(self) -> Tuple[List[UserModel], Optional[str], Optional[str]]:
        """Seleciona todos os usuários (User) disponíveis no banco de dados.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá a lista de objetos usuário selecionados (List[UserModel]), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
        with next(self.db_client()) as db_session:
            users = db_session.query(UserModel).all()
            return (users, None, "")
    
    def select_by_id(self, user_id: int) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        """Seleciona usuário (User) pelo id especifico

        Args:
            user_id (int): ID do usuário (User) que deseja selecionar.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá o objeto usuário selecionado (UserModel), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
        with next(self.db_client()) as db_session:
            user = db_session.query(UserModel).filter(UserModel.id == user_id).first()
            if not user:
                return (None, "UserNotExists", f"User with id {user_id} not exists.")
            return (user, None, "")

    def update(self, user_id: int, new_user_data: dict) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        """Atualiza alguma informação de usuário (User) pelo id especifico dentro dos atributos disponiveis (first_name: str, last_name: str, email: str)

        Args:
            user_id (int): ID do usuário (User) que deseja realizar alguma atualicação no valor de atributo.
            new_user_data(dict): Dicionário com os atributos e seus novos valores para serem atualizados. Os atributos faltantes serão considerados como inalterados, mantendo o valor original.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá o objeto usuário atualizado (UserModel), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
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
        """Deletar algum usuário específico (User) pelo id.

        Args:
            user_id (int): ID do usuário (User) que deseja realizar alguma atualicação no valor de atributo.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá o objeto usuário deletado do banco de dados (UserModel), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
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