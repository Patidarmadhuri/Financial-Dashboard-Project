import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from datetime import timedelta

load_dotenv()

app = Flask(__name__)

# === CONFIG ===
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-jwt-key-2025-change-in-prod")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

# Allow frontend
CORS(app, origins=["http://localhost:3000", "https://financial-dashboard-project-eta.vercel.app"])

# Initialize extensions
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# === DATABASE ===
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI not set in environment")

client = MongoClient(MONGO_URI)
db = client["financial_dashboard"]
charts_collection = db["charts"]
users_collection = db["users"]  # New collection for registered users

# === AUTH ENDPOINTS ===
@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    if users_collection.find_one({"username": username}):
        return jsonify({"error": "User already exists"}), 400

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")
    users_collection.insert_one({"username": username, "password": hashed})
    return jsonify({"message": "User registered successfully"}), 201


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users_collection.find_one({"username": username})
    if user and bcrypt.check_password_hash(user["password"], password):
        token = create_access_token(identity=username)
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid username or password"}), 401


@app.route("/api/protected")
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello {current_user}! This is a protected endpoint."})


@app.route("/")
def home():
    return jsonify({"message": "Financial Dashboard API - LIVE", "endpoints": ["/api/charts", "/api/register", "/api/login"]})


@app.route('/api/charts', methods=['GET'])
def get_charts():
    try:
        quarter = (request.args.get("quarter") or "").strip()
        company = (request.args.get("company") or "").strip().lower()

        quarter_lower = quarter.lower()
        use_quarter = bool(quarter)
        use_median = quarter_lower == "median"

        cursor = charts_collection.find().sort("_id", 1)
        charts = {}
        for idx, doc in enumerate(cursor):
            layout = dict(doc.get("layout", {})) if isinstance(doc.get("layout", {}), dict) else {}
            config = dict(doc.get("config", {})) if isinstance(doc.get("config", {}), dict) else {}
            orig_traces = list(doc.get("data", []))

            filtered_traces = orig_traces

            if company:
                filtered_traces = [tr for tr in filtered_traces if tr.get("name") and company in tr.get("name", "").lower()]

            if use_quarter:
                if use_median:
                    filtered_traces = [tr for tr in filtered_traces if tr.get("name") and "median" in tr.get("name", "").lower()]
                else:
                    filtered_traces = [tr for tr in filtered_traces if tr.get("name") and quarter_lower in tr.get("name", "").lower()]

            # Update chart title for 4th chart
            if idx == 3:
                new_title = "Debt vs Liquid Assets"
                if use_quarter:
                    new_title += f": {quarter}" if not use_median else ": Median Across Quarters"
                if isinstance(layout.get("title"), dict):
                    layout["title"]["text"] = new_title
                else:
                    layout["title"] = {"text": new_title}

            # THIS IS THE IMPORTANT PART: Set yaxis title as object for Plotly to show properly
            if "yaxis" in layout:
                layout["yaxis"]["title"] = {"text": "USD (millions)"}
            else:
                layout["yaxis"] = {"title": {"text": "USD (millions)"}}

            charts[f"chart{idx}"] = {
                "data": filtered_traces,
                "layout": layout,
                "config": config
            }

        return jsonify(charts)

    except Exception as e:
        app.logger.exception("Error in /api/charts")
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    try:
        chart_count = charts_collection.count_documents({})
        user_count = users_collection.count_documents({})
    except Exception:
        chart_count = user_count = 0
    return jsonify({"status": "OK", "db": "Connected", "charts": chart_count, "users": user_count})


if __name__ == "__main__":
    print("Financial Dashboard Backend with Auth - Running on http://localhost:5000")
    app.run(debug=True, port=5000)
