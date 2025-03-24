from tests.config.fixtures.sqlite_session import db_session
from models.user_model import UserModel



def test_db_connection(db_session):
    assert db_session is not None
    assert db_session.bind is not None

def test_user_model(db_session):
    new_user = UserModel(first_name="iury", email="iury@email.com")
    db_session.add(new_user)
    db_session.commit()

    user = db_session.query(UserModel).filter_by(email="iury@email.com").first()

    assert user is not None
    assert user.first_name == "iury"
    assert user.last_name == None
    assert user.email == "iury@email.com"