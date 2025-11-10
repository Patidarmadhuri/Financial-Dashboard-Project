from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_bcrypt import Bcrypt
import os
from dotenv import load_dotenv
from pymongo.errors import ConfigurationError, ConnectionFailure
import time

# Initialize Flask app
app = Flask(__name__)

# Enable CORS (update later for production)
#CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, resources={r"/*": {"origins": [
    "http://localhost:3000",
    "https://financial-dashboard-project-eta.vercel.app"
]}})



# Load environment variables
load_dotenv()

@app.route("/")
def home():
    return jsonify({"message": "Backend is running! Use /api routes."})

# JWT Configuration
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY') or 'temporary-fallback-key-123'
print(f"Loaded JWT_SECRET_KEY: {app.config['JWT_SECRET_KEY'][:10]}...")  # Debug (partial)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 1800  # 30 minutes
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# === CONNECT TO MONGODB ATLAS (CLOUD) ===
MONGO_URI = os.getenv('MONGO_URI')
if MONGO_URI:
    MONGO_URI = MONGO_URI.strip()

for attempt in range(5):
    try:
        client = MongoClient(
            MONGO_URI,
            serverSelectionTimeoutMS=5000,
            connectTimeoutMS=5000
        )
        client.admin.command('ping')
        db = client["financial_dashboard"]
        metrics_collection = db["metrics"]
        users_collection = db["users"]
        print("Connected to MongoDB Atlas!")
        break
    except Exception as e:
        print(f"Attempt {attempt + 1}/5: MongoDB failed: {e}")
        if attempt == 4:
            print("OFFLINE MODE — DB routes will return 500")
            db = metrics_collection = users_collection = None
        else:
            time.sleep(3)

# === ROUTES ===

@app.route('/api/register', methods=['POST'])
def register():

    if users_collection is None:
        return jsonify({"error": "Database not connected"}), 500
    
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    # CHECK IF USER EXISTS
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return jsonify({"error": "Username already exists"}), 409

    try:
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        result = users_collection.insert_one({
            "username": username,
            "password": hashed_password
        })
        print(f"Registered user: {username} (ID: {result.inserted_id})")
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        print(f"Registration error: {str(e)}")  # THIS WILL SHOW THE REAL ERROR
        return jsonify({"error": f"Registration failed: {str(e)}"}), 500


@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = users_collection.find_one({"username": username})
    if not user:
        print("User not found in database")
        return jsonify({"error": "Invalid username or password"}), 401

    # Debugging info
    print(f"Trying login for user: {username}")
    print(f"Stored hash: {user['password']}")

    try:
        if bcrypt.check_password_hash(user["password"], password):
            access_token = create_access_token(identity=username)
            print("✅ Password matched! Login success")
            return jsonify({"token": access_token}), 200
        else:
            print("❌ Password did NOT match!")
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        print(f"Error during password check: {e}")
        return jsonify({"error": "Login error"}), 500


@app.route("/api/dashboard", methods=["GET"])
@jwt_required()
def get_dashboard():
    doc = metrics_collection.find_one({}, {"_id": 0})
    if not doc:
        return jsonify({"error": "No dashboard found"}), 404
    return jsonify(doc)


@app.route("/api/dashboards", methods=["GET"])
@jwt_required()
def get_all_dashboards():
    docs = list(metrics_collection.find({}, {"_id": 0}))
    return jsonify(docs)


@app.route("/api/dashboard/", methods=["POST"])
@jwt_required()
def create_dashboard():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    metrics_collection.insert_one(data)
    return jsonify({"message": "Dashboard data created successfully"}), 201


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
        if result.matched_count == 0:
            return jsonify({"error": "No matching document found"}), 404
        return jsonify({"message": "Dashboard data updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/dashboard/<doc_id>", methods=["DELETE"])
@jwt_required()
def delete_dashboard(doc_id):
    try:
        result = metrics_collection.delete_one({"_id": ObjectId(doc_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "No matching document found"}), 404
        return jsonify({"message": "Dashboard data deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/charts', methods=['GET'])
def get_charts():
    charts = {}
    for doc in db.charts.find():
        chart_id = str(doc['_id'])
        charts[chart_id] = {
            "data": doc.get("data", []),
            "layout": doc.get("layout", {}),
            "config": doc.get("config", {})
        }
    return jsonify(charts)

@app.route('/companies', methods=['GET'])
def get_companies():
    companies = sorted(set(doc.get('CompanyName') for doc in db.metrics.find({}, {'CompanyName': 1})))
    return jsonify(companies)

@app.route('/quarters', methods=['GET'])
def get_quarters():
    quarters = sorted(set(doc.get('ReportQuarter') for doc in db.metrics.find({}, {'ReportQuarter': 1})))
    return jsonify(quarters)

# Health check
@app.route("/health")
def health():
    return jsonify({"status": "Backend is running!", "db": "Atlas connected"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)