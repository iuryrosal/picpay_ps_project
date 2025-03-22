import sqlite3
from faker import Faker


def generate_fake_data():
    fake = Faker("pt_BR")
    name = fake.name()
    fake_data = {
        "first_name": name.split(" ")[0],
        "last_name": " ".join(name.split(" ")[1:]),
        "email": name.split(" ")[0] + "@" + fake.free_email_domain()
    }
    return fake_data


if __name__ == "__main__":
    try:
        with sqlite3.connect("database.db",
                             detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES) as conn:
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
            cursor_obj = conn.cursor()

            table = """ CREATE TABLE IF NOT EXISTS users (
                id CHAR(25) NOT NULL,
                first_name CHAR(25) NOT NULL,
                last_name CHAR(25),
                email VARCHAR(255) NOT NULL
            ); """

            cursor_obj.execute(table)
            for customer_id in range(100):
                fake_customer = generate_fake_data()
                cursor_obj.execute("""
                    INSERT INTO users (id, first_name, last_name, email)
                    VALUES (?, ?, ?, ?);
                """, (customer_id,) + tuple(fake_customer.values()))
                conn.commit()

            cursor_obj.close()
    except sqlite3.OperationalError as e:
        print("Failed during connection with database: ", e)