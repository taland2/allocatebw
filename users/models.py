from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['myapp']


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        db.users.insert_one({'username': self.username, 'password': self.password})

    @staticmethod
    def get_all():
        users = db.users.find()
        return [user for user in users]

    @staticmethod
    def get_by_id(user_id):
        user = db.users.find_one({'_id': ObjectId(user_id)})
        return user

    @staticmethod
    def get_by_username(username):
        user = db.users.find_one({'username': username})
        return user
