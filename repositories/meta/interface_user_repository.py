from abc import ABC, abstractmethod
from typing import Tuple, Optional, List
from models.user_model import UserModel


class IUserRepository(ABC):
    """Interface que representa uma visão genérica do repositório de Usuário, responsável por estabelecer conexão com banco de dados e realizar operações necessárias envolvendo a entidade User.

        Estabelece dependência com a camada de serviço que iteraje com a entidade usuário (User).
    """
    @abstractmethod
    def create(self, first_name: str, email: str, last_name: str = None) -> Tuple[UserModel, Optional[str], Optional[str]]:
        """Realiza criação de um usuário no banco de dados, sendo necessário a adição automática de id com lógica incremental para cada usuário criado.

        Args:
            first_name (str): Primeiro nome do usuário
            email (str): Email atrelado ao usuário
            last_name (str, optional): Sobrenome do usuário. Padrão para None.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá o objeto usuário criado (UserModel), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
        pass
    
    @abstractmethod
    def select_all(self) -> Tuple[List[UserModel], Optional[str], Optional[str]]:
        """Seleciona todos os usuários (User) disponíveis no banco de dados.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá a lista de objetos usuário selecionados (List[UserModel]), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
        pass

    @abstractmethod
    def select_by_id(self, user_id: int) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        """Seleciona usuário (User) pelo id especifico

        Args:
            user_id (int): ID do usuário (User) que deseja selecionar.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá o objeto usuário selecionado (UserModel), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
        pass

    @abstractmethod
    def update(self, user_id: int, new_user_data: dict) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        """Atualiza alguma informação de usuário (User) pelo id especifico dentro dos atributos disponiveis (first_name: str, last_name: str, email: str)

        Args:
            user_id (int): ID do usuário (User) que deseja realizar alguma atualicação no valor de atributo.
            new_user_data(dict): Dicionário com os atributos e seus novos valores para serem atualizados. Os atributos faltantes serão considerados como inalterados, mantendo o valor original.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá o objeto usuário atualizado (UserModel), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
        pass

    @abstractmethod
    def delete_by_id(self, user_id: int) -> Tuple[Optional[UserModel], Optional[str], Optional[str]]:
        """Deletar algum usuário específico (User) pelo id.

        Args:
            user_id (int): ID do usuário (User) que deseja realizar alguma atualicação no valor de atributo.

        Returns:
            Tuple[UserModel, Optional[str], Optional[str]]: Tupla que conterá o objeto usuário deletado do banco de dados (UserModel), título de erro (str) e descrição de erro (str), respectivamente. Em caso de erros, o campo de usuário ficará nulo e teremos o título do erro (str) seguido da descrição do erro (str).
        """
        pass