from faker import Faker
from db.sqllite_client import SqLiteClient, SqLiteBase
from models.user_model import UserModel


def generate_fake_data():
    """Função que irá gerar dados fictícios para usuário (User), envolvendo Email, Primeiro Nome (first_name) e Sobrenome (last_name)

    Returns:
        dict: Dicionário com os dados fictícios gerados. Chaves: first_name, last_name, email
    """
    fake = Faker("pt_BR")
    name = fake.name()
    fake_data = {
        "first_name": name.split(" ")[0],
        "last_name": " ".join(name.split(" ")[1:]),
        "email": name.split(" ")[1] + "@" + fake.free_email_domain()
    }
    return fake_data


if __name__ == "__main__":
    sqlite_client = SqLiteClient()
    SqLiteBase.metadata.create_all(bind=sqlite_client._engine)
    for _ in range(100):
        fake_user = generate_fake_data()
        with next(sqlite_client()) as db_session:
            user = UserModel(first_name=fake_user["first_name"],
                            last_name=fake_user["last_name"],
                            email=fake_user["email"])
            db_session.add(user)
            db_session.commit()
            db_session.refresh(user)