# 🧭 Financial Dashboard API Guide

This guide explains how to use the Flask backend API of the Financial Dashboard.  
You can test all endpoints using **Postman**, **cURL**, or any HTTP client.

---

## 🗃️ Base URL

http://localhost:5000

ruby
Copy code

All API routes start with `/api`.

---

## 📌 Endpoints Overview

| Method | Endpoint | Description |
|:--------|:-----------|:-------------|
| **GET** | `/api/dashboard` | Fetch the latest dashboard data (used by React frontend) |
| **GET** | `/api/dashboards` | Fetch all dashboards (for testing or analytics) |
| **POST** | `/api/dashboard/` | Create a new dashboard entry |
| **PUT** | `/api/dashboard/<ObjectId>` | Update a specific dashboard document |
| **DELETE** | `/api/dashboard/<ObjectId>` | Delete a specific dashboard document |

---

## 🧪 1️⃣ Create Dashboard (POST)

**URL:**  
http://localhost:5000/api/dashboard/

css
Copy code

**Body (JSON):**
```json
{
  "data": [1, 2, 3],
  "layout": { "title": "Test" }
}
Response:

json
Copy code
{
  "message": "Dashboard data created successfully"
}
🔍 2️⃣ View Dashboard (GET)
URL:

bash
Copy code
http://localhost:5000/api/dashboard
Response:

json
Copy code
{
  "data": [1, 2, 3],
  "layout": { "title": "Test" }
}
🔄 3️⃣ Update Dashboard (PUT)
URL:

bash
Copy code
http://localhost:5000/api/dashboard/<ObjectId>
Example:

bash
Copy code
http://localhost:5000/api/dashboard/68ee8cba52f5400824de5d5c
Body (JSON):

json
Copy code
{
  "data": [4, 5, 8],
  "layout": { "title": "Updated Test" }
}
Response:

json
Copy code
{
  "message": "Dashboard data updated successfully"
}
❌ 4️⃣ Delete Dashboard (DELETE)
URL:

bash
Copy code
http://localhost:5000/api/dashboard/<ObjectId>
Example:

bash
Copy code
http://localhost:5000/api/dashboard/68ee8cba52f5400824de5d5c
Response:

json
Copy code
{
  "message": "Dashboard data deleted successfully"
}
🧩 5️⃣ View All Dashboards (GET)
URL:

bash
Copy code
http://localhost:5000/api/dashboards
Response Example:

json
Copy code
[
  {
    "data": [1, 2, 3],
    "layout": { "title": "Test" }
  },
  {
    "data": [4, 5, 6],
    "layout": { "title": "Q2 Report" }
  }
]
🧠 Tips for Analysts
You can import this API collection into Postman and run tests directly.

Only one dashboard (the latest) is shown on the React frontend.

You can use /api/dashboards to verify all entries in the database.

MongoDB Compass can also visualize your data locally.

Maintained by:
👩‍💻 Madhuri Patidar
📅 Updated: October 2025
💬 “Always learning, building, and sharing.”