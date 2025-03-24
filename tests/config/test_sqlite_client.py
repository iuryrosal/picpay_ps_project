from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.sqllite_client import SqLiteBase
from db.sqllite_client import SqLiteClient


class TestSqLiteClient(SqLiteClient):
    """Cliente SQLite para testes, utilizando um banco de dados em memória."""
    
    database_path = "sqlite:///:memory:"

    def __init__(self) -> None:
        self._engine = create_engine(self.database_path)
        self._session = sessionmaker(bind=self._engine, autocommit=False, autoflush=False)
        SqLiteBase.metadata.create_all(self._engine)