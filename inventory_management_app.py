# inventory_management_app.py

from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Mock database
users = {}
inventory = []

# User Registration & Authentication
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if email in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[email] = generate_password_hash(password)
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if email not in users or not check_password_hash(users[email], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    return jsonify({"message": "Login successful"})

# Adding new items to inventory
@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    item_name = data.get('name')
    quantity = data.get('quantity')
    
    if not item_name or quantity is None:
        return jsonify({"error": "Missing required fields"}), 400
    
    inventory.append({"name": item_name, "quantity": quantity})
    return jsonify({"message": "Item added successfully"})

# Searching and sorting items
@app.route('/search', methods=['GET'])
def search_item():
    query = request.args.get('query', '')
    results = [item for item in inventory if query.lower() in item['name'].lower()]
    return jsonify(results)

@app.route('/sort', methods=['GET'])
def sort_items():
    key = request.args.get('key', 'name')
    order = request.args.get('order', 'asc')
    
    try:
        sorted_inventory = sorted(inventory, key=lambda x: x[key], reverse=(order == 'desc'))
        return jsonify(sorted_inventory)
    except KeyError:
        return jsonify({"error": "Invalid sorting key"}), 400

if __name__ == '__main__':
    app.run(debug=True)
