# Financial Dashboard Project  
**Frontend Live Demo**: [
https://financial-dashboard-project-eta.vercel.app/](
https://financial-dashboard-project-eta.vercel.app/)  

**Backend API**: [https://financial-dashboard-project-l853.onrender.com](https://financial-dashboard-project-l853.onrender.com)

**Database MongoDB Atlas**: [https://cloud.mongodb.com/v2/68ee7619d69c31726264c46f#/explorer/68ee7670e30b266a2ee305ca/financial_dashboard](https://cloud.mongodb.com/v2/68ee7619d69c31726264c46f#/explorer/68ee7670e30b266a2ee305ca/financial_dashboard)


Login Details : 
{
  "username": "aapl",
  "password": "987654321"
}


![React](https://img.shields.io/badge/Frontend-React-blue?logo=react)
![Flask](https://img.shields.io/badge/Backend-Flask-black?logo=flask)
![MongoDB](https://img.shields.io/badge/Database-MongoDB%20Atlas-green?logo=mongodb)
![JWT](https://img.shields.io/badge/Auth-JWT%20Secure-orange)
![Vercel](https://img.shields.io/badge/Deployed-Vercel-000000?logo=vercel)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?logo=render)
![Status](https://img.shields.io/badge/Status-LIVE%20&%20SECURE-success)

---

## Overview  
**Turn raw financial data into powerful, real-time insights.**  

The **Financial Dashboard** helps finance teams, analysts, and decision-makers **see trends instantly** through **interactive charts**, **secure login**, and **cloud-powered data**.  

No more Excel chaos — just **clear visuals** for **Cash Position (CCP)**, **Long-Term Debt (LTD)**, and **Revenue Growth** across companies like **AAPL**, **AMZN**, and **KO**.

---

## Live Links  
| Service | URL |
|-------|-----|
| **Frontend (Dashboard)** | [https://financial-dashboard-project.vercel.app](https://financial-dashboard-project.vercel.app) |
| **Backend (API)** | [https://financial-dashboard-project-l853.onrender.com](https://financial-dashboard-project-l853.onrender.com) |
| **Health Check** | [https://financial-dashboard-project-l853.onrender.com/health](https://financial-dashboard-project-l853.onrender.com/health) |

> **Try it now**: Register → Login → Explore live charts!

---

## Features  
- **Secure Login & Registration** – JWT + password hashing  
- **Interactive Charts** – Plotly.js with zoom, filter, and dual-axis  
- **Real-Time KPIs** – Cash, Debt, Revenue, Trends  
- **Cloud Database** – MongoDB Atlas (fully hosted, secure)  
- **REST API** – Full CRUD for data management  
- **Live Deployment** – Vercel (frontend) + Render (backend)  

---
## 🧠 How It Works

```mermaid
graph TD
    A[User Opens Dashboard] --> B[React Frontend on Vercel]
    B --> C[Flask API on Render]
    C --> D[MongoDB Atlas Cloud]
    D --> C
    C --> B
    B --> A
```



   1. You log in → Secure JWT token stored
   2. Charts load → API fetches data from MongoDB Atlas
   3. You see visuals → Interactive, real-time, beautiful
   
The app follows a three-layer architecture:

**React (Frontend) → Flask (Backend) → MongoDB (Database)**


**Data Flow**:

```plaintext
User → React (Login) → Flask (/api/login) → MongoDB (users) → JWT Token
User → React (Dashboard) → Flask (/api/dashboard) → MongoDB (metrics) → Plotly Charts

1.Login: Users authenticate via React, storing JWT in localStorage.
2.Data Fetch: Frontend sends GET /api/dashboard with JWT header.
3.Backend Processing: Flask validates JWT, queries MongoDB metrics, returns Plotly JSON.
4.Visualization: React renders interactive charts via Plotly.js.
5.Data Management: Analysts update metrics via Postman.


🛠️ Tech Stack

Layer        Technology 
Frontend     React, Plotly.js, Axios
Backend      Flask, Flask JWT-Extended, Flask-Bcrypt, Flask-CORS 
Database     MongoDB Atlas (Cloud)
Auth         JWT + Bcrypt
Deployment   Vercel (Frontend), Render (Backend)
Tools        Postman, MongoDB Compass, GitHub, VS Code
Environment  Node.js (v16+), Python (3.8+)



Project Structure
plaintextFinancial-Dashboard-Project/
├── financial-backend/          # Flask API (Render)
│   ├── app.py                  # All routes + JWT + MongoDB
│   ├── .env                    # JWT_SECRET_KEY (local only)
│   └── requirements.txt
├── finacial-dashboard/         # React App (Vercel)
│   ├── src/
│   │   ├── components/
│   │   └── App.js
│   └── package.json
├── docs/                       # Screenshots + API Guide
└── README.md                   # You're reading it!


🚀 Setup Guide (For Developers)
🔍 Prerequisites

| Tool                       | Link                                                       |
|----------------------------|------------------------------------------------------------|
| Node.js (v16+)             | [Download](https://nodejs.org/en)                          |
| Python (3.8+)              | [Download](https://www.python.org/downloads/)              |
| MongoDB                    | [Download](https://www.mongodb.com/try/download/community) |
| Postman (optional)         | [Download](https://www.postman.com/downloads/)             |
| MongoDB Compass (optional) | [Download](https://www.mongodb.com/try/download/compass)


## Backend (Flask)

bash
cd financial-backend
python -m venv venv
.\venv\Scripts\activate    # Windows
pip install -r requirements.txt
python app.py

Runs at: http://localhost:5000


## Frontend (React)
bash
cd finacial-dashboard
npm install
npm start
Runs at: http://localhost:3000


Environment Variables (Production)

Key                  Value (in Render/Vercel)
REACT_APP_API_URL    https://financial-dashboard-project-l853.onrender.comMONGO_URImongodb+srv://madhuri:Dashboard@...
JWT_SECRET_KEY       96d76fa...

API Reference

Endpoint       Method    Auth   Description

/api/register   POST      No    Create user
/api/login      POST      No    Get JWT
/api/dashboard  GET       Yes   Get chart data
/api/dashboard/ POST      Yes   Save new data

Auth Header:
textAuthorization: Bearer <your_jwt_token>


🗄️ Database Setup (MongoDB)

1.Start MongoDB:
bash mongod --dbpath <your-data-path>

2.Create database Financial_dashboard:
bash use Financial_dashboard

3.Create collections:
users: {"username": "testuser8", "password": "<hashed_password>"}
metrics: Plotly JSON (e.g., {"data": [...], "layout": {...}})

4.Register a test user via Postman:
json POST http://localhost:5000/api/register
{
  "username": "testuser8",
  "password": "securepassword1238"
}


📡 API Reference
Explore the API Guide for detailed endpoints, payloads, and Postman examples. Key endpoints:

| Endpoint              | Method | Auth | Description                 |
| --------------------- | ------ | ---- | --------------------------- |
| `/api/register`       | POST   | ❌    | Register a new user         |
| `/api/login`          | POST   | ❌    | Authenticate and return JWT |
| `/api/dashboard`      | GET    | ✅    | Get the latest dashboard    |
| `/api/dashboards`     | GET    | ✅    | Get all dashboards          |
| `/api/dashboard/`     | POST   | ✅    | Create a new dashboard      |
| `/api/dashboard/<id>` | PUT    | ✅    | Update a dashboard          |
| `/api/dashboard/<id>` | DELETE | ✅    | Delete a dashboard          |


Auth Header (for protected routes):
plaintext  Authorization: Bearer <your_token>

Example Login Payload:
json POST http://localhost:5000/api/login
{
  "username": "testuser8",
  "password": "securepassword1238"
}

Response:
json{
  "access_token": "<jwt_token>"
}

## Screenshots

**Dashboard**  
<img src="docs/screenshots/Frontend/Dashboard.png" alt="Dashboard" width="600">

**Login Screen**  
<img src="docs/screenshots/Frontend/login.png" alt="Login" width="600">


## Security
Passwords → Hashed with Bcrypt
Tokens → JWT (30-min expiry)
Database → MongoDB Atlas with auth
CORS → Only allows Vercel frontend
.env → Never pushed to GitHub


## Future Enhancements
Add Admin Panel
Export to PDF
Multiple Companies
Email Alerts
Unit Tests


🤝 Contributing

1. Fork: https://github.com/Patidarmadhuri/Financial-Dashboard-Project

2. Create branch:
bash git checkout -b feature/your-feature

3. Commit and push:
bash git commit -m "Add new feature"
git push origin feature/your-feature

4.Open a Pull Request.

Standards:
Python: PEP 8
React: ESLint
Screenshots: Add to docs/screenshots/

Author
Madhuri Patidar
Full-Stack Developer | Data + Design

"Turning complex data into simple decisions."

madhuri.patidar49@gmail.com
LinkedIn- https://www.linkedin.com/in/madhuri-fullstack-developer/

License
MIT License © 2025 Madhuri Patidar