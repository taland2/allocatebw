from flask import Blueprint, jsonify, request
from users.models import User

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['GET'])
def get_all_users():
    users = User.get_all()
    return jsonify(users)

@users_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_by_id(user_id)
    return jsonify(user)

@users_bp.route('/', methods=['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User(username, password)
    user.save()
    return 'User created successfully!'

@users_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.get_by_username(username)
    if user and user['password'] == password:
        return 'Login successful!'
    else:
        return 'Invalid credentials!'
