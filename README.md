# 💹 Financial Dashboard Project                         🌐 [Live Demo](https://financial-dashboard-project.vercel.app/) 

![React](https://img.shields.io/badge/Frontend-React-blue?logo=react)
![Flask](https://img.shields.io/badge/Backend-Flask-black?logo=flask)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)


### 📘 Overview

Finance teams often struggle to turn raw company data into clear, actionable insights. The **Financial Dashboard Project** was built to solve that problem by transforming scattered financial metrics into interactive visuals and real-time KPIs. Through intuitive charts and secure authentication, it helps teams track performance, analyze trends, and make informed decisions with confidence.  

Built with **React**, **Flask**, and **MongoDB**, this modern dashboard combines powerful backend logic with a clean, responsive frontend for a seamless user experience. It empowers users to monitor company performance with clarity and precision through interactive charts and KPIs such as **Cash & Cash Equivalents (CCP)** and **Long-Term Debt (LTD)** for companies like **AAPL**, **AMZN**, and **KO**.

---

### 🔗 Related Documentation

- 🧠 [Backend README](financial-backend/README.md)
- 💻 [Frontend README](financial-dashboard/README.md)
- 📄 [API Guide](docs/api-guide.md)

---

## 📖 Table of Contents

- [Purpose](#purpose)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup Guide](#setup-guide)
- [API Reference](#api-reference)
- [Screenshots](#screenshots)
- [Security Notes](#security-notes)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

## 🎯 Purpose

The **Financial Dashboard** transforms raw company data into clear, visual insights. It provides a secure, interactive, and user-friendly interface for financial teams, data analysts, and stakeholders to analyze KPIs and track trends in real time.

## ✨ Features

- 🖼️ **Interactive Charts**: Plotly.js visualizations with dual axes and dropdown filters.
- 🔐 **JWT Authentication**: Secure user registration and login using `flask-jwt-extended` and `flask-bcrypt`, implemented by me. JWT tokens are stored in `localStorage` for frontend access.
- ⚙️ **Full REST API**: CRUD operations for managing metrics via Postman.
- 🗃️ **MongoDB Integration**: Dynamic storage for users and chart data.
- 💻 **Modern UI**: Clean, responsive React design.
- 🧩 **Data Ready**: Supports JSON uploads for seamless data integration.

## 🧠 How It Works

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
Database     MongoDB(local)
Tools        Postman, MongoDB Compass 
Environment  Node.js (v16+), Python (3.8+)

📂 Project Structure
plaintextFinancial-Dashboard-Project/
├── financial-backend/            # Flask backend
│   ├── app.py                   # Flask API logic
│   ├── .env                     # JWT secret key
│   ├── requirements.txt         # Python dependencies
│   ├── README.md                # Backend setup guide
├── frontend/                    # React frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── DashboardChart.js # Login and dashboard display
│   │   ├── App.js               # Main React component
│   ├── package.json             # Node.js dependencies
│   ├── README.md                # Frontend setup guide
├── docs/                        # Documentation and visuals
│   ├── screenshots/
│   │   ├── dashboard.png        # Dashboard chart
│   │   ├── login.png            # Login screen
│   ├── api-guide.md             # Detailed API guide
├── .gitignore                   # Git ignore file
├── README.md                    # This file🚀 Setup Guide

🚀 Setup Guide
🔍 Prerequisites

| Tool                       | Link                                                       |
| -------------------------- | ---------------------------------------------------------- |
| Node.js (v16+)             | [Download](https://nodejs.org/en)                          |
| Python (3.8+)              | [Download](https://www.python.org/downloads/)              |
| MongoDB                    | [Download](https://www.mongodb.com/try/download/community) |
| Postman (optional)         | [Download](https://www.postman.com/downloads/)             |
| MongoDB Compass (optional) | [Download](https://www.mongodb.com/try/download/compass)   |


⚙️ Backend Setup (Flask)

1-Navigate to financial-backend/:
bash cd financial-backend

2.Create and activate a virtual environment:
bash python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows

3.Install dependencies:
bash pip install -r requirements.txt

4.Create .env with JWT_SECRET_KEY:
bash python -c "import secrets; print(secrets.token_hex(32))"
Example .env:
plaintext JWT_SECRET_KEY=your_secret_key_here

5.Run the server:
bashpython app.py
➡️ Runs at: http://localhost:5000

Note: Use http://localhost:5000 for local development to avoid SSL errors. For HTTPS, see Security Notes.

🔗 [Backend README](financial-backend/README.md)  


💻 Frontend Setup (React)

1.Navigate to frontend/:
bash cd frontend

2.nstall dependencies:
bash npm install

3.Start the app:
bash npm start
➡️ Runs at: http://localhost:3000

🔗 [Frontend README](financial-dashboard/README.md)


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


📸 Screenshots
Dashboard: Interactive Plotly chart for CCP and LTD trends.
<img src="docs/screenshots/Frontend/Dashboard.png" alt="Dashboard" width="400">
Login Screen: Secure login form.
<img src="docs/screenshots/Frontend/login.png" alt="Login Screen" width="400">

🔒 Security Notes

-> Local Development:
Use http://localhost:5000 to avoid SSL errors.
.env excluded via .gitignore.
MongoDB runs without authentication.


-> Production:
Enable HTTPS:
bash pip install pyOpenSSL
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
 Update app.py: app.run(ssl_context=('cert.pem', 'key.pem'))
Store JWT in HTTP-only cookies.
Use MongoDB Atlas with authentication.
Add rate limiting with flask-limiter.



🌟 Future Enhancements

🌐 Migrate to MongoDB Atlas.
🧭 Add frontend CRUD support.
👥 Implement user roles (Admin/Viewer).
📊 Support dynamic KPI filters and chart types.
✅ Write unit tests for auth endpoints.
🔒 Enhance security with refresh tokens.

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

👩‍💻 Author

Madhuri Patidar
Full Stack Developer | Passionate about clean code and data-driven solutions

💬 “Crafting tools that make financial insights simple and accessible.”
📧 madhuri.patidar49@gmail.com
🔗 LinkedIn linkedin.com/in/madhuri-fullstack-developer/

📄 License
MIT License © 2025 Madhuri Patidar. See LICENSE


