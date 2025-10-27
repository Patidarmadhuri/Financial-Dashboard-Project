
#### 3. API Guide (`docs/api-guide.md`)

This file details the API endpoints, includes analyst-friendly tips, and links back to the main and backend READMEs.

```markdown
# 🧭 Financial Dashboard API Guide

<image-card alt="Flask" src="https://img.shields.io/badge/Backend-Flask-black?logo=flask" ></image-card>
<image-card alt="MongoDB" src="https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb" ></image-card>
<image-card alt="Status" src="https://img.shields.io/badge/Status-Active-success" ></image-card>

### 📘 Overview

The **API Guide** provides a clear reference for the Flask backend of the Financial Dashboard Project. It details endpoints, authentication, and data formats so analysts and developers can easily integrate, test, and manage dashboard metrics. All endpoints use the base URL `http://localhost:5000/api` for local development.

The guide helps teams understand how user actions in the frontend map to backend calls, and ensures secure, accurate access to financial KPIs like **CCP** and **LTD**.

--- 

## 📖 Table of Contents

- [Base URL](#base-url)
- [Endpoints Overview](#endpoints-overview)
- [Authentication Endpoints](#authentication-endpoints)
- [Dashboard Endpoints](#dashboard-endpoints)
- [Tips for Analysts](#tips-for-analysts)
- [Maintainer](#maintainer)
- [Links](#-links)


## 🗃️ Base URL

`http://localhost:5000`

Use **HTTP** for local development to avoid SSL errors. For HTTPS, see [Security Considerations](../financial-backend/README.md#security-considerations).

## 📌 Endpoints Overview

| Method | Endpoint                     | Description                          | Authorization |
|--------|------------------------------|--------------------------------------|---------------|
| POST   | `/api/register`              | Register a new user                 | ❌ No         |
| POST   | `/api/login`                 | Authenticate and get JWT token      | ❌ No         |
| GET    | `/api/dashboard`             | Fetch latest dashboard data         | ✅ Yes        |
| GET    | `/api/dashboards`            | Fetch all dashboard documents       | ✅ Yes        |
| POST   | `/api/dashboard/`            | Create a new dashboard entry        | ✅ Yes        |
| PUT    | `/api/dashboard/<doc_id>`    | Update a dashboard by ObjectId      | ✅ Yes        |
| DELETE | `/api/dashboard/<doc_id>`    | Delete a dashboard by ObjectId      | ✅ Yes        |

**Authorization Header** (for protected endpoints):
```plaintext
Authorization: Bearer <token-from-/api/login>

🔐 Authentication Endpoints
POST /api/register
Register a new user in the users collection.

URL: http://localhost:5000/api/register
Body (JSON):
json{
  "username": "testuser8",
  "password": "securepassword1238"
}

Response (201):
json{"message": "User registered successfully"}


POST /api/login
Authenticate a user and receive a JWT token.

URL: http://localhost:5000/api/login
Body (JSON):
json{
  "username": "testuser8",
  "password": "securepassword1238"
}

Response (200):
json{"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}


📊 Dashboard Endpoints
GET /api/dashboard
Fetch the latest dashboard data for the React frontend.

URL: http://localhost:5000/api/dashboard
Headers: Authorization: Bearer <token>
Response (200):
json{
  "data": [
    {
      "type": "scatter",
      "name": "AAPL_CCP",
      "x": ["2018-12-31T00:00:00", "2019-03-31T00:00:00"],
      "y": [86427, 80092],
      "mode": "lines",
      "line": { "color": "#1f77b4" }
    }
  ],
  "layout": {
    "title": { "text": "CCP and LTD by Company" }
  }
}


GET /api/dashboards
Fetch all dashboard documents for testing or analytics.

URL: http://localhost:5000/api/dashboards
Headers: Authorization: Bearer <token>
Response (200):
json[
  {
    "_id": "68ff3101b43928f7b6dfadaa",
    "data": [
      {
        "type": "scatter",
        "name": "TEST_CCP",
        "x": ["2023-12-31T00:00:00"],
        "y": [50000],
        "mode": "lines",
        "line": { "color": "#FF0000" }
      }
    ],
    "layout": { "title": { "text": "Test Dashboard" } }
  }
]


POST /api/dashboard/
Create a new dashboard entry in the metrics collection.

URL: http://localhost:5000/api/dashboard/
Headers: Authorization: Bearer <token>
Body (JSON):
json{
  "data": [
    {
      "type": "scatter",
      "name": "TEST_CCP",
      "x": ["2023-12-31T00:00:00"],
      "y": [50000],
      "mode": "lines",
      "line": { "color": "#FF0000" }
    }
  ],
  "layout": { "title": { "text": "Test Dashboard" } }
}

Response (201):
json{"message": "Dashboard data created successfully"}


PUT /api/dashboard/<doc_id>
Update a dashboard entry by ObjectId.

URL: http://localhost:5000/api/dashboard/68ff3101b43928f7b6dfadaa
Headers: Authorization: Bearer <token>
Body (JSON):
json{
  "data": [
    {
      "type": "scatter",
      "name": "TEST_CCP_UPDATED",
      "x": ["2023-12-31T00:00:00"],
      "y": [60000],
      "mode": "lines",
      "line": { "color": "#00FF00" }
    }
  ],
  "layout": { "title": { "text": "Updated Dashboard" } }
}

Response (200):
json{"message": "Dashboard data updated successfully"}


DELETE /api/dashboard/<doc_id>
Delete a dashboard entry by ObjectId.

URL: http://localhost:5000/api/dashboard/68ff3101b43928f7b6dfadaa
Headers: Authorization: Bearer <token>
Response (200):
json{"message": "Dashboard data deleted successfully"}


🧠 Tips for Analysts

Use http://localhost:5000 for local testing to avoid SSL errors.
Import the API collection into Postman for easy testing.
Use /api/dashboards to verify all metrics entries.
Only the latest dashboard is shown on the frontend (/api/dashboard).
Use MongoDB Compass to inspect the Financial_dashboard database.
Test with testuser8/securepassword1238 for quick setup.

👩‍💻 Maintainer
Madhuri Patidar
💬 “Building tools to make financial insights accessible!”
📧 madhuri.patidar49@gmail.com
🔗 LinkedIn
📅 Updated: October 2025
🔗 Main README | Backend README


### 🔗 Links

- [Main README](../README.md)  
- [Backend README](../financial-backend/README.md)