import sqlalchemy 
from sqlalchemy import Column, Integer, String
from db.sqllite_client import SqLiteBase

class UserModel(SqLiteBase):
    __tablename__ = "user"
    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("id", name="pk_use"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)