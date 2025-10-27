from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Restrict to frontend

# Load environment variables
load_dotenv()
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or 'temporary-fallback-key-123'  # Temporary fallback
print(f"Loaded JWT_SECRET_KEY: {app.config['JWT_SECRET_KEY']}")  # Debug
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 1800  # 30 minutes
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["Finacial_dashboard"]
metrics_collection = db["metrics"]
users_collection = db["users"]

# Register a new user
@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400
    
    if users_collection.find_one({"username": username}):
        return jsonify({"error": "Username already exists"}), 409
    
    try:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        result = users_collection.insert_one({"username": username, "password": hashed_password})
        print(f"Inserted user {username} with ID {result.inserted_id}")  # Debug
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        print(f"Error inserting user {username}: {str(e)}")  # Debug
        return jsonify({"error": f"Failed to register user: {str(e)}"}), 500

# Login to get JWT token
@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    
    user = users_collection.find_one({"username": username})
    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401
    
    access_token = create_access_token(identity=username)
    return jsonify({"token": access_token}), 200

# GET: fetch the latest dashboard (protected)
@app.route("/api/dashboard", methods=["GET"])
@jwt_required()
def get_dashboard():
    doc = metrics_collection.find_one({}, {"_id": 0})  
    if not doc:
        return jsonify({"error": "No dashboard found"}), 404
    return jsonify(doc)

# GET: fetch all dashboards (protected)
@app.route("/api/dashboards", methods=["GET"])
@jwt_required()
def get_all_dashboards():
    docs = list(metrics_collection.find({}, {"_id": 0}))  # skip _id
    return jsonify(docs)

# POST: add new document (protected)
@app.route("/api/dashboard/", methods=["POST"])
@jwt_required()
def create_dashboard():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    metrics_collection.insert_one(data)
    return jsonify({"message": "Dashboard data created successfully"}), 201

# PUT: update entire document by ObjectId (protected)
@app.route("/api/dashboard/<doc_id>", methods=["PUT"])
@jwt_required()
def update_dashboard(doc_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        result = metrics_collection.update_one(
            {"_id": ObjectId(doc_id)},
            {"$set": data}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    if result.matched_count == 0:
        return jsonify({"error": "No matching document found"}), 404

    return jsonify({"message": "Dashboard data updated successfully"})

# DELETE: delete document by ObjectId (protected)
@app.route("/api/dashboard/<doc_id>", methods=["DELETE"])
@jwt_required()
def delete_dashboard(doc_id):
    try:
        result = metrics_collection.delete_one({"_id": ObjectId(doc_id)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    if result.deleted_count == 0:
        return jsonify({"error": "No matching document found"}), 404

    return jsonify({"message": "Dashboard data deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)