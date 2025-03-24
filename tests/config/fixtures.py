import pytest
from sqlalchemy.orm import Session
from tests.config.test_sqlite_client import TestSqLiteClient 
from tests.config.test_sqlite_user_repository import TestSQLiteUserRepository


@pytest.fixture
def db_session() -> Session:
    """Fornece uma sessão de banco de dados para os testes."""
    db_client = TestSqLiteClient()
    with next(db_client()) as session:
        yield session
