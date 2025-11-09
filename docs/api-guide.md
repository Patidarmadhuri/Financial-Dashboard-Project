
####  API Guide (`docs/api-guide.md`)

This file details the API endpoints, includes analyst-friendly tips, and links back to the main and backend READMEs.

# Financial Dashboard API Guide

![Flask](https://img.shields.io/badge/Backend-Flask-black?logo=flask)
![MongoDB Atlas](https://img.shields.io/badge/Database-MongoDB%20Atlas-green?logo=mongodb)
![JWT](https://img.shields.io/badge/Auth-JWT%20Secure-orange)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?logo=render)
![Status](https://img.shields.io/badge/Status-LIVE%20&%20SECURE-success)

---

## Overview

**Live REST API** for the **Financial Dashboard Project** — fully deployed on **Render** and connected to **MongoDB Atlas (Cloud)**.

All endpoints use:  
**Base URL**: `https://financial-dashboard-project-l853.onrender.com`

> **No local setup needed** — Use **Postman** or **cURL** to test live

---

## 📖 Table of Contents

- [🧭 Financial Dashboard API Guide](#-financial-dashboard-api-guide)
    - [📘 Overview](#-overview)
  - [📖 Table of Contents](#-table-of-contents)
    - [🔗 Links](#-links)
  - [🗃️ Base URL](#️-base-url)
  - [📌 Endpoints Overview](#-endpoints-overview)
    - [🔗 Links](#-links-1)


### 🔗 Links

- [Main README](../README.md)  
- [Backend README](../financial-backend/README.md)

---

## Live API

| Service | URL |
|-------|-----|
| **API Base** | [https://financial-dashboard-project-l853.onrender.com](https://financial-dashboard-project-l853.onrender.com) |
| **Health Check** | [https://financial-dashboard-project-l853.onrender.com/health](https://financial-dashboard-project-l853.onrender.com/health) |
| **Register** | `POST /api/register` |
| **Login** | `POST /api/login` |

---

## 🗃️ Local Base URL

`http://localhost:5000`

Use **HTTP** for local development to avoid SSL errors. For HTTPS, see [Security Considerations](../financial-backend/README.md#security-considerations).

## 🔐 Authentication Flow (Tested in Postman)

#### 1. Register a New User

```http
POST https://financial-dashboard-project-l853.onrender.com/api/register
Content-Type: application/json

{
  "username": "amazon2",
  "password": "hello123456"
}


# Response (201):
json
{ "message": "User registered successfully" }
```

#### 2. Login & Get JWT Token

```httpPOST https://financial-dashboard-project-l853.onrender.com/api/login
Content-Type: application/json

{
  "username": "amazon2",
  "password": "hello123456"
}
Response (200):
json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

Copy this token — Use in Authorization: Bearer <token>

```

### 📊 Dashboard Endpoints
```
Add Header to All Below:

httpAuthorization: Bearer <your_jwt_token>

```

### GET Latest Dashboard Data
```
httpGET https://financial-dashboard-project-l853.onrender.com/api/dashboard
Authorization: Bearer <token>
Response (200):
json{
  "data": [
    {
      "type": "scatter",
      "name": "AAPL_CCP",
      "x": ["2018-12-31", "2019-03-31"],
      "y": [86427, 80092],
      "mode": "lines",
      "line": { "color": "#1f77b4" }
    },
    {
      "type": "scatter",
      "name": "AAPL_LTD",
      "x": ["2018-12-31", "2019-03-31"],
      "y": [93735000, 90201000],
      "mode": "lines",
      "line": { "color": "#ff7f0e" }
    }
  ],
  "layout": {
    "title": { "text": "CCP and LTD Trends" }
  }
}
```

### GET All Dashboards (Admin View)
```
httpGET https://financial-dashboard-project-l853.onrender.com/api/dashboards
Authorization: Bearer <token>
Response (200):
json[
  {
    "_id": "68ff3101b43928f7b6dfadaa",
    "data": [ /* ... */ ],
    "layout": { "title": { "text": "Test Dashboard" } }
  }
]
```

### POST New Dashboard Data

```
httpPOST https://financial-dashboard-project-l853.onrender.com/api/dashboard/
Authorization: Bearer <token>
Content-Type: application/json

{
  "data": [
    {
      "type": "scatter",
      "name": "TEST_CCP",
      "x": ["2025-01-01"],
      "y": [75000],
      "mode": "lines",
      "line": { "color": "#FF0000" }
    }
  ],
  "layout": { "title": { "text": "New Test Chart" } }
}
Response (201):
json{ "message": "Dashboard data created successfully" }
```

### PUT Update Dashboard
```
httpPUT https://financial-dashboard-project-l853.onrender.com/api/dashboard/68ff3101b43928f7b6dfadaa
Authorization: Bearer <token>
Content-Type: application/json

{
  "data": [
    {
      "type": "scatter",
      "name": "TEST_CCP_UPDATED",
      "x": ["2025-01-01"],
      "y": [85000],
      "mode": "lines",
      "line": { "color": "#00FF00" }
    }
  ],
  "layout": { "title": { "text": "Updated Chart" } }
}
Response (200):
json{ "message": "Dashboard data updated successfully" }
```

### DELETE Dashboard
```

httpDELETE https://financial-dashboard-project-l853.onrender.com/api/dashboard/68ff3101b43928f7b6dfadaa
Authorization: Bearer <token>
Response (200):
json{ "message": "Dashboard data deleted successfully" }
```

### Quick Test Users (Live)
```
Username,Password
aapl,987654321
amazon2,hello123456

Use these in Postman → Login → Copy Token → Test Dashboard
```
### Postman Collection (Import This) 
```
{
  "info": {
    "name": "Financial Dashboard API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Register",
      "request": {
        "method": "POST",
        "header": [{ "key": "Content-Type", "value": "application/json" }],
        "body": { "mode": "raw", "raw": "{\n  \"username\": \"newuser\",\n  \"password\": \"pass123\"\n}" },
        "url": "https://financial-dashboard-project-l853.onrender.com/api/register"
      }
    },
    {
      "name": "Login",
      "request": {
        "method": "POST",
        "header": [{ "key": "Content-Type", "value": "application/json" }],
        "body": { "mode": "raw", "raw": "{\n  \"username\": \"aapl\",\n  \"password\": \"987654321\"\n}" },
        "url": "https://financial-dashboard-project-l853.onrender.com/api/login"
      }
    },
    {
      "name": "Get Dashboard",
      "request": {
        "method": "GET",
        "header": [
          { "key": "Authorization", "value": "Bearer {{token}}" }
        ],
        "url": "https://financial-dashboard-project-l853.onrender.com/api/dashboard"
      }
    }
  ],
  "variable": [
    { "key": "token", "value": "" }
  ]
}

Save as Financial-Dashboard-API.postman_collection.json → Import in Postman
```


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

```


### 🧠 Tips for Analysts
```
Frontend uses: /api/dashboard (latest only)
Use /api/dashboards to see all entries
MongoDB Atlas: View Live Data
JWT expires in 30 mins — Re-login if needed
CORS: Only allows Vercel frontend
```

### 🔗 Links

- [Main README](../README.md)  
- [Backend README](../financial-backend/README.md)


#### 👩‍💻 Maintainer
Madhuri Patidar
💬 “Building tools to make financial insights accessible!”
📧 madhuri.patidar49@gmail.com
🔗 LinkedIn
📅 Updated: October 2025
🔗 Main README | Backend README


