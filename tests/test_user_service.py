from tests.config.fixtures import user_service, mock_sqlite_user_repository

from models.user_model import UserModel


def test_create_user(user_service, mock_sqlite_user_repository):
    mock_user = UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com")
    mock_sqlite_user_repository.create.return_value = (mock_user, None, None)

    result = user_service.create_user(first_name="Iury",
                                      email="rosal@gmail.com",
                                      last_name="Rosal")

    assert result == mock_user

def test_get_user(user_service, mock_sqlite_user_repository):
    mock_user = UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com")
    mock_sqlite_user_repository.select_by_id.return_value = (mock_user, None, None)

    result = user_service.get_user(user_id=1)

    assert result == mock_user

def test_get_user_not_exist(user_service, mock_sqlite_user_repository):
    user_id = 1 # Does Not Exist
    mock_sqlite_user_repository.select_by_id.return_value = (None, "UserDoesNotExist", f"User with id {user_id} does not exist.")

    result = user_service.get_user(user_id=user_id)

    assert result == ("UserDoesNotExist", f"User with id {user_id} does not exist.")

def test_get_all_users(user_service, mock_sqlite_user_repository):
    mock_users = [UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com")]
    mock_sqlite_user_repository.select_all.return_value = (mock_users, None, None)

    result = user_service.get_all_users()

    assert result == mock_users

def test_update_user(user_service, mock_sqlite_user_repository):
    mock_user = [UserModel(id=1, first_name="Iury", last_name="Lima", email="rosal@gmail.com")]
    mock_sqlite_user_repository.update.return_value = (mock_user, None, None)

    result = user_service.update_user(user_id=1, new_user_data={"last_name": "Lima"})

    assert result == mock_user

def test_delete_user(user_service, mock_sqlite_user_repository):
    mock_user = [UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com")]
    mock_sqlite_user_repository.delete_by_id.return_value = (mock_user, None, None)

    result = user_service.delete_user(user_id=1)

    assert result == mock_user