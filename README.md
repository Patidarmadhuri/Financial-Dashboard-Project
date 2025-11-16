# Financial Dashboard Project  

**Frontend Live Demo**: [
https://financial-dashboard-project-eta.vercel.app/](
https://financial-dashboard-project-eta.vercel.app/)  

**Backend API**: [https://financial-dashboard-project-l853.onrender.com](https://financial-dashboard-project-l853.onrender.com)


> **Just open the link — no login required!**


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

The **Financial Resilience Dashboard** displays **4 interactive charts** built from real company data (CCP, LTD, Debt Coverage, Liquid Assets) — **no login required**.

Perfect for analysts, students, or anyone exploring financial trends across **AAPL, AMZN, KO**, and more.

---
#### 🧩 What This Dashboard Shows
```
-> Revenue
-> Expenses
-> Profit
-> Debt
-> Cash flow
-> KPI comparisons
-> Interactive line, bar, and pie charts
-> Hover, zoom, toggle series, filter by period
```
---

#### 👥 Who This Project Is For

```
# Non-technical users - 
Just open the live demo link and explore the charts
No install, no login
Everything is point-and-click

# Data analysts - 
Fetch clean JSON from the API
Build your own dashboards in Excel, Python, Power BI
Import sample data from data/sample_metrics.json

# Developers - 
Full-stack app: React + Node.js + Express + MongoDB
Clear folder structure
Easy environment setup (see below)

```
---
### Live Links  
| Service | URL |
|-------|-----|
| **Frontend (Dashboard)** | [https://financial-dashboard-project-eta.vercel.app](https://financial-dashboard-project-eta.vercel.app) |
| **Backend (API)** | [https://financial-dashboard-project-l853.onrender.com](https://financial-dashboard-project-l853.onrender.com) |
| **Charts API** | [https://financial-dashboard-project-l853.onrender.com/api/charts](https://financial-dashboard-project-l853.onrender.com/api/charts) |
| **Health Check** | [https://financial-dashboard-project-l853.onrender.com/health](https://financial-dashboard-project-l853.onrender.com/health) |

> **Try it now**: Register → Login → Explore live charts!

---

## Features  
- **4 Interactive Charts** – Plotly.js with zoom, hover, and export  
- **Public Access** – No login, no JWT  
- **Real Data** – Sourced from MongoDB Atlas (CCP, LTD, ratios, heatmaps)  
- **Responsive Design** – Works on mobile, tablet, desktop  
- **Live Deployment** – Vercel + Render (auto-deploy on push)

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
   


```mermaid
graph TD
    A[User Opens Dashboard] --> B[React Frontend<br/>on Vercel]
    B --> C[GET /api/charts]
    C --> D[Flask Backend<br/>on Render]
    D --> E[MongoDB Atlas<br/>Cloud]
    E --> D
    D --> B
    B --> F[5 Interactive<br/>Plotly Charts]
```



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

```

### 🚀 Setup Guide (For Developers)
🔍 Prerequisites

| Tool                       | Link                                                       |
|----------------------------|------------------------------------------------------------|
| Node.js (v16+)             | [Download](https://nodejs.org/en)                          |
| Python (3.8+)              | [Download](https://www.python.org/downloads/)              |
| MongoDB                    | [Download](https://www.mongodb.com/try/download/community) |
| Postman (optional)         | [Download](https://www.postman.com/downloads/)             |
| MongoDB Compass (optional) | [Download](https://www.mongodb.com/try/download/compass)


## Backend (Flask)
```
bash
cd financial-backend
python -m venv venv
.\venv\Scripts\activate    # Windows
pip install -r requirements.txt
python app.py

Runs at: "http://localhost:5000"

```
## Frontend (React)
```
bash
cd finacial-dashboard
npm install
npm start
Runs at: "http://localhost:3000"
```

### Environment Variables (Production)
```
 Key                   Value (in Render/Vercel) 

 REACT_APP_API_URL      https://financial-dashboard-project-l853.onrender.comMONGO_URImongodb+srv://madhuri:Dashboard@... 

 JWT_SECRET_KEY         96d76fa... 


```


## 🗄️ Database (MongoDB Atlas - Cloud)
```
**No local setup needed** — Everything runs in the **cloud**!
```
### Already Set Up:
- **Database**: `Financial_dashboard`
- **Collections**: `users`, `metrics`
- **Connection**: Secure via `MONGO_URI` in Render
- **Test User**: `aapl` / `987654321`

### How to Add Data (Optional - For Testing)
```

Use **Postman** or **cURL** to register a new user:

POST https://financial-dashboard-project-l853.onrender.com/api/register
Content-Type: application/json
bash
{
  "username": "newuser",
  "password": "yourpassword123"
}

```

### 📡 API Reference 

Explore the API Guide for detailed endpoints, payloads, and Postman examples. Key endpoints:

| Endpoint              | Method | Auth | Description                 |
| --------------------- | ------ | ---- | --------------------------- |
| `/api/charts`         | GET    | ❌    | Returns all 4 charts as Plotly JSON         |
| `/api/register`       | POST   | ❌    | Register a new user         |
| `/api/login`          | POST   | ❌    | Authenticate and return JWT |
| `/api/dashboard`      | GET    | ✅    | Get the latest dashboard    |
| `/api/dashboards`     | GET    | ✅    | Get all dashboards          |
| `/api/dashboard/`     | POST   | ✅    | Create a new dashboard      |
| `/api/dashboard/<id>` | PUT    | ✅    | Update a dashboard          |
| `/api/dashboard/<id>` | DELETE | ✅    | Delete a dashboard          |

```
Auth Header (for protected routes):
plaintext  Authorization: Bearer <your_token>

Example Login Payload:
json POST " http://localhost:5000/api/login "
{
  "username": "testuser8",
  "password": "securepassword1238"
}

Response:
json{
  "access_token": "<jwt_token>"
}

```

### Screenshots

**Financial Resilience Dashboard**

<img src="docs\screenshots\Frontend\Financial_Dashbord_Screenshot.png" alt="Dashboard" width="600">


#### 🔗 Links

- [Frontend README](financial-dashboard/README.md)  
- [Backend README](financial-backend/README.md)  
- [API Guide](docs/api-guide.md)
  

#### Security

```
1. Passwords → Hashed with Bcrypt
2. Tokens → JWT (30-min expiry)
3. Database → MongoDB Atlas with auth
4. CORS → Only allows Vercel frontend
```

## Future Enhancements

```
1. Add company filter dropdown
2. Add quarter/year selector
3. Export charts to PDF
4. Add dark mode toggle

```

#### 🚀 Developer Quickstart

```
1. Clone the project
git clone https://github.com/Patidarmadhuri/Financial-Dashboard-Project
cd Financial-Dashboard-Project

2. Environment Variables
Create .env in backend:
MONGO_URI=
JWT_SECRET_KEY=

Create .env in frontend:
REACT_APP_API_URL=

Do not commit secrets. Use .env.example for sharing variable names.

3. Install dependencies
Backend
cd backend
npm install

Frontend
cd ../frontend
npm install

4. Run the project locally
Backend
npm start

Server runs at: http://localhost:5000

Frontend
npm start

App runs at: http://localhost:3000

```

#### 💾 Sample Data for Analysts

```
You’ll find example financial metrics in:
/data/sample_metrics.json

Import into:
Excel
Python (Pandas)
Power BI
Tableau
```

### 🤝 Contributing
```
1. Fork: https://github.com/Patidarmadhuri/Financial-Dashboard-Project

2. Create branch:
bash git checkout -b feature/your-feature

3. Commit and push:
bash git commit -m "Add new feature"
git push origin feature/your-feature

4.Open a Pull Request.
```
#### Standards:
```
Python: PEP 8
React: ESLint
Screenshots: Add to docs/screenshots/
```

### Author
Madhuri Patidar
```
Full-Stack Developer | Data + Design

"Turning complex data into simple decisions."

Email ID- madhuri.patidar49@gmail.com
LinkedIn- https://www.linkedin.com/in/madhuri-fullstack-developer/

```

License
MIT License © 2025 Madhuri Patidar