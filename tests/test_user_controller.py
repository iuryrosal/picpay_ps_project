from tests.config.fixtures import mock_user_service
from tests.config.fixtures import fastapi_app_client

from models.user_model import UserModel


def test_create_user(fastapi_app_client, mock_user_service):
    mock_user_service.create_user.return_value = UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com")

    user_data = {"first_name": "Iury", "last_name": "Rosal", "email": "rosal@gmail.com"}
    response = fastapi_app_client.post("/users/", json=user_data)

    assert response.status_code == 201
    assert response.json()["first_name"] == "Iury"
    assert response.json()["last_name"] == "Rosal"
    assert response.json()["email"] == "rosal@gmail.com"

def test_create_user_without_mandatory_attribute(fastapi_app_client, mock_user_service):
    mock_user_service.create_user.return_value = UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com")

    user_data = {"first_name": "Iury"}
    response = fastapi_app_client.post("/users/", json=user_data)

    assert response.status_code == 422


def test_get_users(fastapi_app_client, mock_user_service):
    mock_user_service.get_all_users.return_value = [
        UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com"),
        UserModel(id=2, first_name="Davi", last_name="Oliveira", email="davi@gmail.com"),
    ]

    response = fastapi_app_client.get("/users/")

    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["first_name"] == "Iury"
    assert response.json()[1]["first_name"] == "Davi"


def test_get_user_success(fastapi_app_client, mock_user_service):
    mock_user_service.get_user.return_value = UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com")

    response = fastapi_app_client.get("/users/1")

    assert response.status_code == 200
    assert response.json()["first_name"] == "Iury"


def test_get_user_not_found(fastapi_app_client, mock_user_service):
    mock_user_service.get_user.return_value = ("UserDoesNotExist", "User with id 99 not exists.")

    response = fastapi_app_client.get("/users/99")

    assert response.status_code == 404
    assert response.json()["code"] == "UserDoesNotExist"


def test_update_user(fastapi_app_client, mock_user_service):
    mock_user_service.update_user.return_value = UserModel(id=1, first_name="Iury Atualizado", last_name="Rosal", email="rosal@gmail.com")

    update_data = {"first_name": "Iury Atualizado"}
    response = fastapi_app_client.put("/users/1", json=update_data)

    assert response.status_code == 200
    assert response.json()["first_name"] == "Iury Atualizado"
    assert response.json()["last_name"] == "Rosal"
    assert response.json()["email"] == "rosal@gmail.com"


def test_delete_user(fastapi_app_client, mock_user_service):
    mock_user_service.delete_user.return_value = UserModel(id=1, first_name="Iury", last_name="Rosal", email="rosal@gmail.com")

    response = fastapi_app_client.delete("/users/1")

    assert response.status_code == 200
    assert response.json()["code"] == "UserDeleted"


def test_delete_user_not_found(fastapi_app_client, mock_user_service):
    mock_user_service.delete_user.return_value = ("UserDoesNotExist", "User with id 99 not exists.")

    response = fastapi_app_client.delete("/users/99")

    assert response.status_code == 404
    assert response.json()["code"] == "UserDoesNotExist"