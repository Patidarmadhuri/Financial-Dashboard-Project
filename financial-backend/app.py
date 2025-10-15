from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["Finacial_dashboard"]
collection = db["metrics"]

# GET: fetch the latest dashboard (for React frontend)
@app.route("/api/dashboard", methods=["GET"])
def get_dashboard():
    doc = collection.find_one({}, {"_id": 0})  
    if not doc:
        return jsonify({"error": "No dashboard found"}), 404
    return jsonify(doc)

# GET: fetch all dashboards (for Postman/testing)
@app.route("/api/dashboards", methods=["GET"])
def get_all_dashboards():
    docs = list(collection.find({}, {"_id": 0}))  # skip _id
    return jsonify(docs)

# POST: add new document
@app.route("/api/dashboard/", methods=["POST"])
def create_dashboard():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    collection.insert_one(data)
    return jsonify({"message": "Dashboard data created successfully"}), 201

# PUT: update entire document by ObjectId
@app.route("/api/dashboard/<doc_id>", methods=["PUT"])
def update_dashboard(doc_id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    try:
        result = collection.update_one(
            {"_id": ObjectId(doc_id)},
            {"$set": data}
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    if result.matched_count == 0:
        return jsonify({"error": "No matching document found"}), 404

    return jsonify({"message": "Dashboard data updated successfully"})

# DELETE: delete document by ObjectId
@app.route("/api/dashboard/<doc_id>", methods=["DELETE"])
def delete_dashboard(doc_id):
    try:
        result = collection.delete_one({"_id": ObjectId(doc_id)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    if result.deleted_count == 0:
        return jsonify({"error": "No matching document found"}), 404

    return jsonify({"message": "Dashboard data deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
