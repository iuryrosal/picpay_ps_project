from typing import List, Union, Tuple
from models.user_model import UserModel
from abc import ABC, abstractmethod


class IUserService(ABC):
    """Interface que representa uma visão genérica do serviço de Usuário, responsável por estabelecer as regras de negócio desse contexto.

        Depende do repositório de usuário para conectar com o banco de dados para realizar as operações necessárias.

        Estabelece dependência com a camada de controller que iteraje com a entidade usuário (User).
    """
    @abstractmethod
    def create_user(self, first_name: str, last_name: str, email: str)-> Union[UserModel, Tuple[str, str]]:
        """Cria usuário (User) novo para o negócio, contendo as informações de primeiro nome (first_name), sobrenome (last_name) e email. 

        Quando um usuário é criado no banco de dados, um ID (identificador único) é gerado e retornado dentro do objeto de usuário (UserModel).

        Args:
            first_name (str): Primeiro nome do usuário
            email (str): Email atrelado ao usuário
            last_name (str, optional): Sobrenome do usuário. Padrão para None por ser um campo optativo.

        Returns:
            Union[UserModel, Tuple[str, str]]: Retorna o usuário criado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        pass
    
    @abstractmethod
    def get_user(self, user_id: int)-> Union[UserModel, Tuple[str, str]]:
        """Obtem usuário (User) existente no negócio, contendo as informações de primeiro nome (first_name), sobrenome (last_name) e email. É necessário um ID (identificador único) para especificar qual usuário deseja selecionar.

        Args:
            user_id (int): ID do usuário (User) que deseja selecionar.

        Returns:
            Union[UserModel, Tuple[str, str]]: Retorna o usuário selecionado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        pass
    
    @abstractmethod
    def get_all_users(self) -> Union[List[UserModel], Tuple[str, str]]:
        """Coleta todos os usuários (User) existentes no negócio, contendo as informações de primeiro nome (first_name), sobrenome (last_name) e email de cada um.

        Returns:
            Union[List[UserModel], Tuple[str, str]]: Retorna a lista de usuários selecionado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        pass

    @abstractmethod
    def update_user(self, user_id: int, new_user_data: dict) -> Union[UserModel, Tuple[str, str]]:
        """Atualiza alguma informação de usuário (User) dentro dos atributos disponiveis (first_name: str, last_name: str, email: str)

        Args:
            user_id (int): ID do usuário (User) que deseja realizar alguma atualicação no valor de atributo.
            new_user_data(dict): Dicionário com os atributos e seus novos valores para serem atualizados. Os atributos faltantes serão considerados como inalterados, mantendo o valor original.

        Returns:
            Union[UserModel, Tuple[str, str]]: Retorna o usuário atualizado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> Union[UserModel, Tuple[str, str]]:
        """Deletar algum usuário específico (User) pelo id.

        Args:
            user_id (int): ID do usuário (User) que deseja realizar alguma atualicação no valor de atributo.


        Returns:
            Union[UserModel, Tuple[str, str]]: Retorna o usuário deletado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        pass