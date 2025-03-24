import pytest
from sqlalchemy.orm import Session
from tests.config.sqlite_client_test import TestSqLiteClient 


@pytest.fixture
def db_session() -> Session:
    """Fornece uma sessão de banco de dados para os testes."""
    db_client = TestSqLiteClient()
    with next(db_client()) as session:
        yield session