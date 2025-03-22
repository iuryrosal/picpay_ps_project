import sqlalchemy 
from db.sqllite_client import SqLiteBase

class User(SqLiteBase):
    __tablename__ = "user"
    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("id", name="pk_use")
    )

    id = sqlalchemy.Column("id", sqlalchemy.String, nullable=False)
    first_name = sqlalchemy.Column("first_name", sqlalchemy.String, nullable=False)
    last_name = sqlalchemy.Column("last_name", sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column("email", sqlalchemy.String, nullable=False)