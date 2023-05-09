from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['resource_management']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inventory')
def inventory():
    resources = db.resources.find()
    return render_template('inventory.html', resources=resources)

@app.route('/edit_resource/<resource_id>', methods=['GET', 'POST'])
def edit_resource(resource_id):
    resource = db.resources.find_one({'_id': ObjectId(resource_id)})
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        consumed_by_id = request.form['consumed_by_id']
        if consumed_by_id == 'None':
            consumed_by_id = None
        else:
            consumed_by_id = ObjectId(consumed_by_id)
        db.resources.update_one({'_id': ObjectId(resource_id)}, {'$set': {'name': name, 'quantity': quantity, 'consumed_by_id': consumed_by_id}})
        return redirect(url_for('inventory'))
    users = db.users.find()
    return render_template('edit_resource.html', resource=resource, users=users)

@app.route('/users')
def users():
    users = db.users.find()
    return render_template('users.html', users=users)

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        db.users.insert_one({'name': name})
        return redirect(url_for('users'))
    return render_template('create_user.html')

if __name__ == '__main__':
    app.run(debug=True)
