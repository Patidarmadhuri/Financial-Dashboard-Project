# Backend README (`financial-backend/README.md`)

This file covers the Flask backend, includes ToC links, and references the API Guide for detailed endpoints.

# 💻 Financial Dashboard Backend


![Flask](https://img.shields.io/badge/Backend-Flask-black?logo=flask)
![MongoDB](https://img.shields.io/badge/Database-MongoDB%20Atlas-green?logo=mongodb)
![JWT](https://img.shields.io/badge/Auth-JWT%20Secure-orange)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?logo=render)
![Status](https://img.shields.io/badge/Status-LIVE%20&%20SECURE-success)

---

## Live API

[https://financial-dashboard-project-l853.onrender.com](https://financial-dashboard-project-l853.onrender.com)

**Health Check**: [https://financial-dashboard-project-l853.onrender.com/health](https://financial-dashboard-project-l853.onrender.com/health)

---
---

### Features

- Public endpoint `/api/charts` → returns 4 ready-to-use Plotly JSON charts  
- JWT authentication (register/login) — included for learning  
- MongoDB Atlas cloud database (no local setup needed)  
- Fully deployed on Render (auto-deploy on push)

---

## 📘 Overview

**Full REST API** with:
- **JWT authentication** (login/register)
- **CRUD operations** on dashboard data
- **Public `/api/charts`** (used by frontend)
- **MongoDB Atlas** (cloud database)

> **Frontend uses only `/api/charts` (public)**  
> **Use `/api/register`, `/api/login` for learning & testing**


---

## 📖 Table of Contents

- [Backend README (`financial-backend/README.md`)](#backend-readme-financial-backendreadmemd)
- [💻 Financial Dashboard Backend](#-financial-dashboard-backend)
  - [Live API](#live-api)
    - [Features](#features)
  - [📘 Overview](#-overview)
  - [📖 Table of Contents](#-table-of-contents)
    - [🔗 Links](#-links)
  - [🎯 Purpose](#-purpose)
  - [🛠️ Tech Stack](#️-tech-stack)
  - [📂 Directory Structure](#-directory-structure)
    - [🚀 Setup Instructions](#-setup-instructions)
    - [Production (Render)](#production-render)
    - [🔗 API Reference](#-api-reference)
  - [Authentication Endpoints](#authentication-endpoints)
        - [POST /api/register](#post-apiregister)
    - [🔒 Security Considerations](#-security-considerations)
    - [🤝 Contributing](#-contributing)
      - [🔗 Main README | API Guide](#-main-readme--api-guide)
    - [🔗 Links](#-links-1)

### 🔗 Links

- [Main README](../README.md)  
- [API Guide](../docs/api-guide.md)

## 🎯 Purpose

The backend manages user authentication and financial metrics (e.g., CCP, LTD) for the Financial Dashboard, serving Plotly-compatible JSON to the React frontend.

## 🛠️ Tech Stack

| Component       | Technology                     |
|-----------------|--------------------------------|
| **Backend**     | Flask, Flask-JWT-Extended, Flask-Bcrypt, Flask-CORS |
| **Database**    | MongoDB Atlas (Cloud)               |
| **Tools**       | Postman, MongoDB Compass       |
| **Deployment** |Render (Free Tier)                  |
| **Auth**       | JWT + Bcrypt      |
| **Environment** | Python (3.8+)                  |

## 📂 Directory Structure

```plaintext
financial-backend/
├── app.py                   # Flask API logic
├── .env                     # JWT secret key
├── requirements.txt         # Python dependencies
├── venv/                    # Virtual environment
├── README.md                # This file
```



### 🚀 Setup Instructions

```
Prerequisites
Python (3.8+): Download
MongoDB: Download
Postman: Download (optional)

Steps
1. Navigate to financial-backend/:
cd financial-backend
python -m venv venv
.\venv\Scripts\activate    # Windows
pip install -r requirements.txt

2. Create and activate a virtual environment:
bash python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows

3. Install dependencies:
bash pip install -r requirements.txt

4. Create .env with JWT_SECRET_KEY:
bash python -c "import secrets; print(secrets.token_hex(32))"

Example .env:
JWT_SECRET_KEY=your_secret_key_here
MONGO_URI=mongodb://localhost:27017/Financial_dashboard
JWT_SECRET_KEY=96d76fa338579b534161c94670f4eb46d0a0232cee45e09dd2304b896dc63d6b

5. Ensure MongoDB is running at mongodb://localhost:27017.

6. Run the server:
bash python app.py
➡️ Runs at: http://localhost:5000

Note: Use http://localhost:5000 for local development to avoid SSL errors. For HTTPS, see Security Considerations.
```

### Production (Render)

```
Environment Variables (Set in Render Dashboard):

Key         Value
MONGO_URI   mongodb+srv://madhuri:Dashboard@cluster0.3ezqwh1.mongodb.net/Financial_dashboard?retryWrites=true&w=majority

JWT_SECRET_KEY  96d76fa338579b534161c94670f4eb46d0a0232cee45e09dd2304b896dc63d6b

Start Command: gunicorn app:app
```

### 🔗 API Reference


```
See the API Guide for detailed endpoints, payloads, and Postman examples.

 Method     Endpoint          Auth       Description

GET           /api/charts      No        Public — 5 Plotly charts
POST          /api/register    No        register user
POST          /api/login       no        Get JWT
GET           /api/dashboard   Yes       Protected data
GET           /api/dashboards  Yes      All entries
POST          /api/dashboard/  Yes      create
PUT/DELETE    /api/dashboard/
              <doc_id>         Yes     update, delete

 See API Guide for full details
```

## Authentication Endpoints

##### POST /api/register
**Description**: Register a new user.
**Payload**:
```json
{
  "username": "string",
  "password": "string"
}
Response:

201: {"message": "User registered"}
400: {"error": "User already exists"}

POST /api/login
Description: Authenticate user and return JWT.
Payload:
json{
  "username": "string",
  "password": "string"
}
Response:
200: {"access_token": "<jwt_token>"}
401: {"error": "Invalid credentials"}

```



### 🔒 Security Considerations

```
Local Development:
 Use http://localhost:5000 to avoid SSL errors.
 .env excluded via .gitignore.
 MongoDB runs without authentication.

1. Passwords → Bcrypt hashed
2. JWT → 30-min expiry
3. CORS → Only Vercel frontend



```




### 🤝 Contributing

```
1. Fork: https://github.com/Patidarmadhuri/Financial-Dashboard-Project

2. Create branch:
bash git checkout -b feature/backend-your-feature

3. Commit and push:
bash git commit -m "Add backend feature"
git push origin feature/backend-your-feature

4. Open a Pull Request.

Standards:
Code Style: PEP 8 for Python
Issues: Use GitHub Issues

```

#### 🔗 Main README | API Guide

### 🔗 Links

- [Main README](../README.md)  
- [API Guide](../docs/api-guide.md)