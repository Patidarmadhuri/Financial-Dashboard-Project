# 🌐 Financial Dashboard Frontend

<image-card alt="React" src="https://img.shields.io/badge/Frontend-React-blue?logo=react" ></image-card>
<image-card alt="Status" src="https://img.shields.io/badge/Status-Active-success" ></image-card>

This is the React frontend for the **Financial Dashboard Project**, rendering interactive financial charts using Plotly.js and handling user authentication for visualizing KPIs like Cash and Cash Equivalents (CCP) and Long-Term Debt (LTD) for companies like AAPL, AMZN, and KO.

## 📖 Table of Contents

- [🌐 Financial Dashboard Frontend](#-financial-dashboard-frontend)
  - [📖 Table of Contents](#-table-of-contents)
  - [🎯 Purpose](#-purpose)
  - [🛠️ Tech Stack](#️-tech-stack)
  - [📂 Directory Structure](#-directory-structure)

## 🎯 Purpose

The frontend provides a user-friendly interface for financial teams to log in, fetch data from the Flask backend, and visualize metrics via interactive Plotly.js charts.

## 🛠️ Tech Stack

| Component       | Technology                     |
|-----------------|--------------------------------|
| **Frontend**    | React, Plotly.js, Axios        |
| **Environment** | Node.js (v16+)                 |

## 📂 Directory Structure

```plaintext
frontend/
├── src/
│   ├── components/
│   │   ├── DashboardChart.js # Login and dashboard display
│   ├── App.js               # Main React component
├── public/
├── package.json             # Node.js dependencies
├── README.md                # This file

🚀 Setup Instructions
Prerequisites
Node.js (v16+): Download
Backend running at http://localhost:5000 (see Backend README).

Setup

1. Navigate to frontend/:
bash cd frontend

2. Install dependencies:
bash npm install

3 .Start the app:
bash npm start
➡️ Runs at: http://localhost:3000


🔄 How It Works

1. Login: Users authenticate via a React form, sending POST to /api/login, storing JWT in localStorage.
2. Data Fetch: Sends GET to /api/dashboard with Authorization: Bearer <token>.
3. Visualization: DashboardChart.js renders Plotly JSON as interactive charts.

Data Flow:
User → React (Login) → Flask (/api/login) → JWT Token
User → React (Dashboard) → Flask (/api/dashboard) → Plotly Chart

📸 Screenshots
Dashboard: Interactive Plotly chart for CCP and LTD trends.
<img src="../docs/screenshots/Frontend/Dashboard.png" alt="Dashboard" width="400">
Login Screen: Secure login form.
<img src="../docs/screenshots/Frontend/login.png" alt="Login Screen" width="400">

🤝 Contributing

1. Fork: https://github.com/Patidarmadhuri/Financial-Dashboard-Project

2. Create branch:
bash git checkout -b feature/frontend-your-feature

3. Commit and push:
bash git commit -m "Add frontend feature"
git push origin feature/frontend-your-feature

4. Open a Pull Request.


Standards:
Code Style: ESLint for React
Issues: Use GitHub Issues
Screenshots: Add to ../docs/screenshots/

🔗 Main README | API Guide