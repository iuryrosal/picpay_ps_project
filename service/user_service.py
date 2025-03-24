from typing import List, Union, Tuple
from repositories.meta.interface_user_repository import IUserRepository
from models.user_model import UserModel
from service.meta.interface_user_service import IUserService


class UserService(IUserService):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def __handle_response_from_repository(self,
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
        user, error_type, error_msg = self.repository.create(first_name=first_name,
                                                             last_name=last_name,
                                                             email=email)
        return self.__handle_response_from_repository(user, error_type, error_msg)

    def get_user(self, user_id: int) -> Union[UserModel, Tuple[str, str]]:
        user, error_type, error_msg = self.repository.select_by_id(user_id)
        return self.__handle_response_from_repository(user, error_type, error_msg)

    def get_all_users(self) -> Union[List[UserModel], Tuple[str, str]]:
        users, error_type, error_msg  = self.repository.select_all()
        return self.__handle_response_from_repository(users, error_type, error_msg)

    def update_user(self, user_id: int, new_user_data: dict) -> Union[UserModel, Tuple[str, str]]:
        user, error_type, error_msg  = self.repository.update(user_id, new_user_data)
        return self.__handle_response_from_repository(user, error_type, error_msg)

    def delete_user(self, user_id: int) -> Union[UserModel, Tuple[str, str]]:
        user, error_type, error_msg  = self.repository.delete_by_id(user_id)
        return self.__handle_response_from_repository(user, error_type, error_msg)