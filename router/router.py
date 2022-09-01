from flask import request, jsonify, Blueprint
from controllers.user_controller import users
from werkzeug.security import generate_password_hash

user_bp = Blueprint("users", __name__)


@user_bp.route("/users", methods=["GET"])
def get_users():
    result = users.get_users()
    return jsonify(result)

@user_bp.route('/user/<id>', methods=['GET'])
def get_user_by_id(id):
    result = users.get_user_by_id(id)
    return jsonify(result)


@user_bp.route("/register", methods=["POST"])
def create_user():
    
    data = request.get_json()


    hash = generate_password_hash(data['password'], method='sha256')
    name = data["name"]
    surname = data["surname"]
    email = data["email"]
    password = hash
    result = users.create_user(name, surname, email, password)
    return jsonify(result)


@user_bp.route("/update/user", methods=["PUT"])
def update_user():
    data = request.get_json()
    id = data["id"]
    name = data["name"]
    surname = data["surname"]
    email = data["email"]
    result = users.update_user(id, name, surname, email)
    return jsonify(result)


@user_bp.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    result = users.delete_user(id)
    return jsonify(result)
