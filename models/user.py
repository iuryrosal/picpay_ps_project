import sqlalchemy 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint("id", name="pk_use")
    )

    id = sqlalchemy.Column("id", sqlalchemy.String, nullable=False)
    first_name = sqlalchemy.Column("first_name", sqlalchemy.String, nullable=False)
    last_name = sqlalchemy.Column("last_name", sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column("email", sqlalchemy.String, nullable=False)
    created_at = sqlalchemy.Column("created_at", sqlalchemy.Datetime(timezone=True), nullable=False)
    updated_at = sqlalchemy.Column("updated_at", sqlalchemy.Datetime(timezone=True), nullable=True)