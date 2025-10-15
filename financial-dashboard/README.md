# ⚛️ Financial Dashboard – Frontend

The **frontend** of the Financial Dashboard is built with **React** and **Plotly.js**, providing an interactive interface that visualizes financial data from the backend API.

---

## 🚀 Features

- Displays real-time data fetched from the Flask backend
- Interactive charts using Plotly.js
- Responsive layout (auto-adjusts to screen size)
- Simple, modular React component structure

---

## 🗂️ Folder Structure

frontend/
│
├── src/
│   ├── components/
│   │   └── DashboardChart.js   # Core chart component
│   ├── App.js
│   └── index.js
│
├── package.json
└── README.md
⚙️ Setup Instructions
Step 1: Install dependencies
bash
Copy code
cd frontend
npm install
Step 2: Start the development server
bash
Copy code
npm start
The app will run at:
👉 http://localhost:3000

🔗 API Connection
The frontend automatically fetches data from the Flask backend endpoint:
http://localhost:5000/api/dashboard

Make sure your backend is running before you start the React app.

🧩 Component Overview
DashboardChart.js
This is the main React component that:

Fetches dashboard data from the backend API

Passes it to the Plotly component for visualization

Displays a loading message if data isn’t ready

jsx
Copy code
fetch("http://localhost:5000/api/dashboard")
  .then(res => res.json())
  .then(data => setPlotData(data))
  .catch(err => console.error("Error fetching dashboard:", err));
🧭 Future Improvements
Add multiple chart types and tabs

Integrate filters (e.g., by year, region, or metric)

Display API errors or “no data” messages more clearly

Add UI for adding or updating charts without Postman

Made with ❤️ by Madhuri Patidar
💬 “Always learning, building, and sharing.”


