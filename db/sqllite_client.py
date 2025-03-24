from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

SqLiteBase = declarative_base()

class SqLiteClient:
    """Cliente para realizar conexão com o banco de dados SqLite responsável por dados de usuários (User) atrelado ao caminho db/database.db,

    O uso do objeto instanciado dessa classe como uma execução de função (__call__) é retornado um gerador que é responsável por ativar a sessão e encerrando a sessão no final da iteração. Pode ser utilizado como gerenciador de contexto.

    Atributos de Instância:
        _engine: Responsável por instanciar um objeto engine atrelado ao banco de dados e drivers necessários.
        _session: Responsável por instanciar um objeto Session utilizando o _engine para realizar as operações necessárias.
    """
    database_path = "sqlite:///db/database.db"

    def __init__(self) -> None:
        self._engine = create_engine(self.database_path)
        self._session = sessionmaker(bind=self._engine, autocommit=False, autoflush=False)
    
    def __call__(self) -> Session:
        session_local = self._session()
        try:
            yield session_local
        finally:
            session_local.close()
    
    def _get_session(self):
        return next(self.__call__())