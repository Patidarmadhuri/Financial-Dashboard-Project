# Financial Dashboard Project  

### 🔗 Live Demo  

**Frontend**: [https://financial-dashboard-project-eta.vercel.app/](https://financial-dashboard-project-eta.vercel.app/)  

**Backend API**: [https://financial-dashboard-project-l853.onrender.com](https://financial-dashboard-project-l853.onrender.com)



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

The **Financial Resilience Dashboard** displays **4 interactive charts** built from real company data (CCP, LTD, Debt Coverage, Liquid Assets).

Perfect for analysts, students, or anyone exploring financial trends across **AAPL, AMZN, KO**, and more.

---
#### 🧩 What This Dashboard Shows

This dashboard shows key financial trends for multiple companies.  
It loads four charts directly from a live Flask API:

- **CCP (Capital Consumption Pattern)**
- **LTD (Long-Term Debt)**
- **Liquid Assets**
- **Debt Coverage Ratio**

All charts are interactive. You can zoom, hover, export, or toggle lines with one click.



---

#### 👥  Who Can Use This


#### ✔ Non-Technical Users  
Just open the website and explore the charts.  
No installation, no login, nothing to set up.

#### ✔ Data Analysts  
Fetch clean JSON from the API and use it in:
- Excel  
- Power BI  
- Pandas  
- Tableau  

#### ✔ Developers  
A complete **React + Flask + MongoDB** project.  
Easy to read and easy to extend.


---
### Important  Links  
| Purpose  | URL |
|-------|-----|
| **Frontend (Dashboard)** | [https://financial-dashboard-project-eta.vercel.app](https://financial-dashboard-project-eta.vercel.app) |
| **Backend (API)** | [https://financial-dashboard-project-l853.onrender.com](https://financial-dashboard-project-l853.onrender.com) |
| **All Charts API** | [https://financial-dashboard-project-l853.onrender.com/api/charts](https://financial-dashboard-project-l853.onrender.com/api/charts) |
| **Health Check** | [https://financial-dashboard-project-l853.onrender.com/health](https://financial-dashboard-project-l853.onrender.com/health) |

###### All links are public and work without authentication.
---

## Features  
- **4 Interactive Charts** – Plotly.js with zoom, hover, and export  
- **Public Access** – No login, no JWT  
- **Real Data** – Sourced from MongoDB Atlas (CCP, LTD, ratios, heatmaps)  
- **Responsive Design** – Works on mobile, tablet, desktop  
- **Live Deployment** – Vercel + Render (auto-deploy on push)

---
## 🧠 How It Works

1. React frontend opens.  
2. It calls the Flask API `/api/charts`.  
3. Flask loads chart data from MongoDB Atlas.  
4. React uses Plotly.js to draw the charts on the screen.
   
### Data Flow Diagram   

```mermaid
graph TD
    A[User Opens Dashboard] --> B[React Frontend on Vercel]
    B --> C[Flask API on Render]
    C --> D[MongoDB Atlas Cloud]
    D --> C
    C --> B
    B --> A
```
   1. Charts load → API fetches data from MongoDB Atlas
   2. You see visuals → Interactive, real-time, beautiful
   


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


### 🛠️ Tech Stack
```

Layer        Technology 
Frontend     React, Plotly.js, Axios
Backend      Flask, Flask JWT-Extended, Flask-Bcrypt, Flask-CORS 
Database     MongoDB Atlas (Cloud)
Auth         JWT + Bcrypt
Deployment   Vercel (Frontend), Render (Backend)
Tools        Postman, MongoDB Compass, GitHub, VS Code
Environment  Node.js (v16+), Python (3.8+)

```

### 📁 Project Structure
```
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


### Backend (Flask)
```
bash
cd financial-backend
python -m venv venv
.\venv\Scripts\activate    # Windows
pip install -r requirements.txt
python app.py

Runs at: "http://localhost:5000"

```
### Frontend (React)
```
bash
cd finacial-dashboard
npm install
npm start
Runs at: "http://localhost:3000"
```

#### Environment Variables (Production)
```
 Key                   Value (in Render/Vercel) 

 REACT_APP_API_URL      https://financial-dashboard-project-l853.onrender.comMONGO_URImongodb+srv://madhuri:Dashboard@... 

 JWT_SECRET_KEY         96d76fa... 


```


### 🗄️ Database (MongoDB Atlas - Cloud)
```
**No local setup needed** — Everything runs in the **cloud**!
```

###### Already Set Up:
- **Database**: `Financial_dashboard`
- **Collections**: `users`, `metrics`, `charts`


#### How to Add Data (Optional - For Testing)
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
##### What You'll See 

**Public access** – Open demo, explore 4 interactive charts from real data (2018-2023, 12 companies: AAPL, AMZN, KO + more). Hover/zoom for details.

| Chart | Type | Shows | Sample (AAPL 2023Q4) |
|-------|------|-------|---------------------|
| **CCP Trends** | Line | Cash conversion over quarters | $73,100M |
| **LTD Trends** | Line | Long-term debt growth | $106,042M |
| **CCP/LTD Ratio** | Line/Heatmap | Coverage balance (0-2.65 scale) | 0.69 |
| **Debt vs. Assets** | Scatter | Debt (Y) vs. Cash (X), size=risk | Bubble ~22 |
| **Company Overview** | Scatter | Medians/benchmarks by ticker | CCP median: $9,707M |                               (Data: Millions USD, MongoDB-sourced.)
-----


##### For Analysts & Devs
**Sample Metrics (AAPL 2018Q4):**
```json
{
  "ticker": "AAPL",
  "quarter": "2018Q4",
  "ccp": 86427,
  "ltd": 102761,
  "ratio": 0.84
}
```


#### 📡 API Reference 


| Endpoint      | Method | Description                 |
| ------------- | ------ | --------------------------- |
| `/api/charts` | GET    | Returns all 4 Plotly charts |
| `/health`     | GET    | Server status               |
dashboard          |

Example response (shortened)
```
[
  {
    "_id": "6911f3ada80b859252090ff6",
    "data": [...],
    "layout": {...}
  }
]
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


### Screenshots

**Financial Resilience Dashboard**

1. CCP & LTD by Company
   
 <img src="docs\screenshots\Frontend\fig1_CCP_and_Ltd_by_Company.png" alt="Dashboard" width="600">
   
2. Debt Coverage Ratio
   
 <img src="docs\screenshots\Frontend\fig2_Ration_CCP_LTD_By_Companies.png" alt="Dashboard" width="600">
   
3. Financial Resilience Heatmap
   
   <img src="docs\screenshots\Frontend\fig3_Financial_Resilience_Heatmap.png" alt="Dashboard" width="600">

4. Debt vs Liquid Assets (all)
   
   <img src="docs\screenshots\Frontend\fig4_Dept_VS_Liquid_Assets.png" alt="Dashboard" width="600">

#### 🔗 Links

- [Frontend README](financial-dashboard/README.md)  
- [Backend README](financial-backend/README.md)  
- [API Guide](docs/api-guide.md)
  

#### Security

Even though the system is public, the backend is protected at server level:

1. Database stored in MongoDB Atlas
2. CORS protected
3. Read-only API


#### Future Enhancements


1. Company dropdown selector
2. Quarter/year filter
3. Export entire dashboard to PDF
4. Dark mode toggle


#### 🚀 Developer Quickstart

```
# 1. Clone the project
git clone https://github.com/Patidarmadhuri/Financial-Dashboard-Project
cd Financial-Dashboard-Project

# 2. Set environment variables

# Backend (.env)
MONGO_URI=
JWT_SECRET_KEY=

# Frontend (.env)
REACT_APP_API_URL=

# Remember: Do NOT commit your secrets! Use a .env.example file for sharing.

# 3. Install dependencies

# Backend
cd financial-backend
pip install -r requirements.txt

# Frontend
cd ../financial-dashboard
npm install

# 4. Run locally

# Backend
python app.py
# Runs on http://localhost:5000

# Frontend
npm start
# Runs on http://localhost:3000


```

### 🤝 Contributing
```
# 1. Fork the repo
git clone https://github.com/Patidarmadhuri/Financial-Dashboard-Project

# 2. Create a new feature branch
git checkout -b feature/your-feature

# 3. Commit your changes
git commit -m "Add new feature"

# 4. Push branch to your fork
git push origin feature/your-feature

# 5. Open a Pull Request

```
#### Code Style Standards:


Python: Follow PEP 8
React: Use ESLint rules
Add screenshots for new UI features in /docs/screenshots/


### Author
Madhuri Patidar
Full-Stack Developer 
"Turning complex data into simple decisions."
 madhuri.patidar49@gmail.com
 https://www.linkedin.com/in/madhuri-fullstack-developer/



License
MIT License © 2025 Madhuri Patidar