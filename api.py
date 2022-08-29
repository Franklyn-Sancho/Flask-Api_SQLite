from flask import Flask, Blueprint
from config.db import new_table
from controllers.user_controller import users
from router.router import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)

@app.route("/")
def hello():
    return "Hello World"


# retorna todos os usuários cadastrados

if __name__ == "__main__":
    new_table()
    app.run(debug=True)
