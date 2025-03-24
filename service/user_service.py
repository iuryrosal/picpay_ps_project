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
        """Adapta retorno do repositório para o novo formato da camada serviço, agregando regras de negócio para melhorar o contexto do erro.
        
        No fim, é esperado que seja retornado o objeto esperado em questão (em caso de sucesso) ou a Tupla de erro em caso de falha, contento título e descrição do erro, respectivamente.

        Args:
            object_expected (Union[UserModel, List[UserModel], None]): Conterá o objeto esperado no retorno do repositório, normalmente sendo o UserModel. Em caso de falha detectada no repositório, esse objeto será None.
            error_type (Union[str, None]): Título do erro reportado pelo repositório, normalmente indicado de maneira resumida e única o que aconteceu. Ex: 'UserNotExists' para indicar que o ID fornecido não existe no banco de dados.
            error_msg (Union[str, None]): Mensagem que prover mais detalhes da falha, normalmente atrelando campos dinâmicos que ajudaram a entender a origem do problema. Ex: No caso de 'UserNotExists', a mensagem conterá o ID que foi fornecido e não localizou nenhum usuário atrelado a ele.

        Returns:
            Union[UserModel, List[UserModel], Tuple[str, str]]: Retorna objeto esperado (UserModel ou List[UserModel]) ou Tupla de erro (Titulo (str), Descrição (str))
        """
        if object_expected:
            return object_expected
        else:
            return (error_type, error_msg)

    def create_user(self, first_name: str, email: str, last_name: str = None) -> Union[UserModel, Tuple[str, str]]:
        """Cria usuário (User) novo para o negócio, contendo as informações de primeiro nome (first_name), sobrenome (last_name) e email. 

        Quando um usuário é criado no banco de dados, um ID (identificador único) é gerado e retornado dentro do objeto de usuário (UserModel).

        Args:
            first_name (str): Primeiro nome do usuário
            email (str): Email atrelado ao usuário
            last_name (str, optional): Sobrenome do usuário. Padrão para None por ser um campo optativo.

        Returns:
            Union[UserModel, Tuple[str, str]]: Retorna o usuário criado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        user, error_type, error_msg = self.repository.create(first_name=first_name,
                                                             last_name=last_name,
                                                             email=email)
        return self._handle_response_from_repository(user, error_type, error_msg)

    def get_user(self, user_id: int) -> Union[UserModel, Tuple[str, str]]:
        """Obtem usuário (User) existente no negócio, contendo as informações de primeiro nome (first_name), sobrenome (last_name) e email. É necessário um ID (identificador único) para especificar qual usuário deseja selecionar.

        Args:
            user_id (int): ID do usuário (User) que deseja selecionar.

        Returns:
            Union[UserModel, Tuple[str, str]]: Retorna o usuário selecionado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        user, error_type, error_msg = self.repository.select_by_id(user_id)
        return self._handle_response_from_repository(user, error_type, error_msg)

    def get_all_users(self) -> Union[List[UserModel], Tuple[str, str]]:
        """Coleta todos os usuários (User) existentes no negócio, contendo as informações de primeiro nome (first_name), sobrenome (last_name) e email de cada um.

        Returns:
            Union[List[UserModel], Tuple[str, str]]: Retorna a lista de usuários selecionado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        users, error_type, error_msg  = self.repository.select_all()
        return self._handle_response_from_repository(users, error_type, error_msg)

    def update_user(self, user_id: int, new_user_data: dict) -> Union[UserModel, Tuple[str, str]]:
        """Atualiza alguma informação de usuário (User) dentro dos atributos disponiveis (first_name: str, last_name: str, email: str)

        Args:
            user_id (int): ID do usuário (User) que deseja realizar alguma atualicação no valor de atributo.
            new_user_data(dict): Dicionário com os atributos e seus novos valores para serem atualizados. Os atributos faltantes serão considerados como inalterados, mantendo o valor original.

        Returns:
            Union[UserModel, Tuple[str, str]]: Retorna o usuário atualizado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        user, error_type, error_msg  = self.repository.update(user_id, new_user_data)
        return self._handle_response_from_repository(user, error_type, error_msg)

    def delete_user(self, user_id: int) -> Union[UserModel, Tuple[str, str]]:
        """Deletar algum usuário específico (User) pelo id.

        Args:
            user_id (int): ID do usuário (User) que deseja realizar alguma atualicação no valor de atributo.


        Returns:
            Union[UserModel, Tuple[str, str]]: Retorna o usuário deletado no banco de dados pelo repositório (UserModel) ou uma Tupla com informações de erro (título e descrição, respectivamente) em caso de alguma falha esperada/identificada (Tuple[str, str]).
        """
        user, error_type, error_msg  = self.repository.delete_by_id(user_id)
        return self._handle_response_from_repository(user, error_type, error_msg)


if __name__ == "__main__":
    from repositories.sqlite_user_repository import SQLiteUserRepository
    user_repo = SQLiteUserRepository()
    service = UserService(user_repo)

    response = service.create_user("João", "Silva", "joao@email.com")
    print("Usuário criado:", {response})

    user_id = response.__dict__["id"]
    response = service.get_user(user_id)
    print("Usuário encontrado:", response)

    print("Lista de usuários:", service.get_all_users())

    response = service.update_user(user_id, "João", "Santos", "joao_santos@email.com")
    print("Usuário atualizado:", response)

    response = service.delete_user(user_id)
    print("Usuário removido:", response) 