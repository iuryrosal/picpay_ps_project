from repositories.sqlite_user_repository import SQLiteUserRepository

from tests.config.test_sqlite_client import TestSqLiteClient

class TestSQLiteUserRepository(SQLiteUserRepository):
    """Repositório para cenário de Testes no contexto de SQLite do UserRepository, instanciando o TestSqLiteClient para se conectar com o SQLite em nivel de memória.
    """
    def __init__(self) -> None:
        self.db_client = TestSqLiteClient()