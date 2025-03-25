from tests.config.fixtures import user_repo
from models.user_model import UserModel
import pytest


def test_create_user_with_all_attributes(user_repo):
    user, err_code, err_msg = user_repo.create(first_name="Iury", last_name="Rosal", email="rosal@gmail.com")

    assert user is not None
    assert user.id is not None
    assert user.first_name == "Iury"
    assert user.last_name == "Rosal"
    assert user.email == "rosal@gmail.com"
    assert err_code is None
    assert err_msg is None

def test_create_user_with_only_mandatory_attributes(user_repo):
    user, err_code, err_msg = user_repo.create(first_name="Iury", email="rosal@gmail.com")

    assert user is not None
    assert user.id is not None
    assert user.first_name == "Iury"
    assert user.last_name ==  None
    assert user.email == "rosal@gmail.com"
    assert err_code is None
    assert err_msg is None

def test_create_user_without_mandatory_attributes(user_repo):
    with pytest.raises(TypeError):
        user_repo.create(first_name="Iury")

def test_select_all_users(user_repo):
    for _ in range(10):
        user, _, _ = user_repo.create(first_name="Iury", last_name="Rosal", email="rosal@gmail.com")

    users, err_code, err_msg = user_repo.select_all()

    assert users is not None
    assert isinstance(users, list)
    assert all(isinstance(item, UserModel) for item in users)
    assert len(users) == 10
    assert err_code is None
    assert err_msg is None

def test_select_by_id(user_repo):
    user, _, _ = user_repo.create(first_name="Iury", email="rosal@gmail.com")

    retrieved_user, err_code, err_msg = user_repo.select_by_id(user.id)
    
    assert retrieved_user is not None
    assert retrieved_user.id == user.id
    assert retrieved_user.first_name == user.first_name
    assert retrieved_user.last_name == user.last_name
    assert retrieved_user.email == user.email
    assert err_code is None
    assert err_msg is None

def test_select_by_id_not_exists(user_repo):
    user_id = 1 # not exists
    user, err_code, err_msg = user_repo.select_by_id(user_id)
    
    assert user is None
    assert err_code == "UserDoesNotExist"
    assert err_msg == f"User with id {user_id} does not exist."

def test_update_user(user_repo):
    user, _, _ = user_repo.create(first_name="Iury", last_name="Rosal", email="rosal@gmail.com")
    new_user_data = {
        "first_name": "Davi"
    }
    updated_user, err_code, err_msg = user_repo.update(user_id=user.id, new_user_data=new_user_data)

    assert updated_user is not None
    assert updated_user.id == user.id
    assert updated_user.first_name == "Davi"
    assert updated_user.last_name == user.last_name
    assert updated_user.email == user.email
    assert err_code is None
    assert err_msg is None


def test_update_user_not_exists(user_repo):
    user_id = 1 # not exists
    new_user_data = {
        "first_name": "Davi"
    }
    updated_user, err_code, err_msg = user_repo.update(user_id=user_id, new_user_data=new_user_data)

    assert updated_user is None
    assert err_code == "UserDoesNotExist"
    assert err_msg == f"User with id {user_id} does not exist."

def test_delete_user(user_repo):
    user, _, _ = user_repo.create(first_name="Iury", last_name="Rosal", email="rosal@gmail.com")

    deleted_user, err_code, err_msg = user_repo.delete_by_id(user.id)

    assert deleted_user is not None
    assert deleted_user.id == user.id
    assert deleted_user.first_name == user.first_name
    assert deleted_user.last_name == user.last_name
    assert deleted_user.email == user.email
    assert err_code is None
    assert err_msg is None

    retrieved_user, err_code, err_msg = user_repo.select_by_id(user.id)
    assert retrieved_user is None
    assert err_code == "UserDoesNotExist"


def test_delete_user_not_exists(user_repo):
    user_id = 1 # not exists

    deleted_user, err_code, err_msg = user_repo.delete_by_id(user_id)

    assert deleted_user is None
    assert err_code == "UserDoesNotExist"
    assert err_msg == f"User with id {user_id} does not exist."