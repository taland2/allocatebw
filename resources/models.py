from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['myapp']


class Resource:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def save(self):
        db.resources.insert_one({'name': self.name, 'quantity': self.quantity})

    @staticmethod
    def get_all():
        resources = db.resources.find()
        return [resource for resource in resources]

    @staticmethod
    def get_by_id(resource_id):
        resource = db.resources.find_one({'_id': ObjectId(resource_id)})
        return resource

    def update(self):
        db.resources.update_one({'_id': ObjectId(self.id)}, {'$set': {'name': self.name, 'quantity': self.quantity}})

    @staticmethod
    def delete(resource_id):
        db.resources.delete_one({'_id': ObjectId(resource_id)})
