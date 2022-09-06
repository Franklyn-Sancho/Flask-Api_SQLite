from config.db import connect_db
from uuid import uuid4

class users:

    # retornar todos os usuários
    def get_users():
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        return cursor.fetchall()

    def get_user_by_id(id):
        db = connect_db()
        cursor = db.cursor()
        sql = "SELECT * FROM users WHERE id = ?"
        cursor.execute(sql, [id])
        return cursor.fetchall()

    # registrar um usuário
    def create_user(name, surname, email, password):
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO users(name, surname, email, password) VALUES (?,?,?,?)"
        cursor.execute(sql, [name, surname, email, password])
        db.commit()
        return "Novo usuário cadastrado com sucesso"

    # atualizar um usuário
    def update_user(id, name, surname, email):
        db = connect_db()
        cursor = db.cursor()
        sql = "UPDATE users SET name = ?, surname = ?, email = ? WHERE id = ?"
        cursor.execute(sql, [name, surname, email, id])
        db.commit()
        return "O usuário " + name + " foi atualizado com sucesso"

    # deletar um usuário
    def delete_user(id):
        db = connect_db()
        cursor = db.cursor()
        sql = "DELETE FROM users WHERE id = ?"
        cursor.execute(sql, [id])
        db.commit()
        return "Usuário de id: " + id + " deletado com sucesso"
