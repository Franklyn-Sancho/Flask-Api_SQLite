import sqlite3

DATABASE = "users.db"

# conectando ao banco de dados.
def connect_db():
    conn = sqlite3.connect(DATABASE)
    return conn


# criando uma tabela
def new_table():
    users = [
        """CREATE TABLE IF NOT EXISTS USERS(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL 

        )"""
    ]

    db = connect_db()
    cursor = db.cursor()
    for user in users:
        cursor.execute(user)
