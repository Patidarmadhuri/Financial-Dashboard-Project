from pymongo import MongoClient
import json

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["Finacial_dashboard"]  # Your local DB name
collection = db["metrics"]

# Fetch all data
data = list(collection.find())

# Convert ObjectId to string
for doc in data:
    doc["_id"] = str(doc["_id"])

# Save to JSON
with open("metrics.json", "w") as f:
    json.dump(data, f, indent=2)

print("Exported metrics.json — Ready for Atlas!")