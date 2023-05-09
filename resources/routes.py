from flask import Blueprint, jsonify, request
from resources.models import Resource

resources_bp = Blueprint('resources', __name__, url_prefix='/resources')

@resources_bp.route('/', methods=['GET'])
def get_all_resources():
    resources = Resource.get_all()
    return jsonify(resources)

@resources_bp.route('/<resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = Resource.get_by_id(resource_id)
    return jsonify(resource)

@resources_bp.route('/', methods=['POST'])
def create_resource():
    name = request.json.get('name')
    quantity = request.json.get('quantity')
    resource = Resource(name, quantity)
    resource.save()
    return 'Resource created successfully!'

@resources_bp.route('/<resource_id>', methods=['PUT'])
def edit_resource(resource_id):
    name = request.json.get('name')
    quantity = request.json.get('quantity')
    db.resources.update_one({'_id': ObjectId(resource_id)}, {'$set': {'name': name, 'quantity': quantity}})
    return 'Resource updated successfully!'

@resources_bp.route('/<resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    db.resources.delete_one({'_id': ObjectId(resource_id)})
    return 'Resource deleted successfully!'
