from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

SqLiteBase = declarative_base()

class SqLiteClient:
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