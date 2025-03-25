import pytest
from fastapi import FastAPI
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient

from controller.v1.user_controller import UserController, get_user_service

from tests.config.test_sqlite_client import TestSqLiteClient 
from tests.config.test_sqlite_user_repository import TestSQLiteUserRepository


@pytest.fixture
def db_session() -> Session:
    """Fornece uma sessão de banco de dados para os testes."""
    db_client = TestSqLiteClient()
    with next(db_client()) as session:
        yield session

@pytest.fixture
def user_repo():
    return TestSQLiteUserRepository()

@pytest.fixture
def mock_user_service():
    mock_service = MagicMock()
    mock_service.create_user = MagicMock()
    mock_service.get_all_users = MagicMock()
    mock_service.get_user = MagicMock()
    mock_service.update_user = MagicMock()
    mock_service.delete_user = MagicMock()
    return mock_service

@pytest.fixture
def fastapi_app_client(mock_user_service):
    app = FastAPI()
    app.include_router(UserController.router)
    client = TestClient(app)
    app.dependency_overrides[get_user_service] = lambda: mock_user_service
    return client