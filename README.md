# 💹 Financial Dashboard Project

![Dashboard Screenshot](docs/screenshots/)

An **interactive financial dashboard** that visualizes data from **MongoDB** using **React (frontend)**, **Flask (backend)**, and **Plotly.js (charts)**.  
Built for developers, analysts, and non-technical users to easily view and understand financial metrics.

---

## 🧠 Project Overview

This dashboard connects a **Flask API** to a **MongoDB** database and displays interactive charts in **React**.  
Data analysts can update metrics via APIs, and the dashboard automatically reflects those updates.

| Stack | Technology |
|:------|:------------|
| **Frontend** | React + Plotly.js |
| **Backend** | Flask (Python) |
| **Database** | MongoDB Compass (Local) |
| **API Testing** | Postman |
| **Goal** | Visualize and manage financial metrics easily |

---

## ✨ Key Features

✅ Interactive charts using **Plotly.js**  
✅ Real-time data visualization powered by **MongoDB**  
✅ Full **CRUD** functionality (Create, Read, Update, Delete)  
✅ Tested with **Postman**  
✅ Modular folder structure for collaboration  

---

## 🗂️ Folder Structure

```plaintext
Financial-Dashboard-Project/
│
├── backend/                     # Flask backend
│   ├── app.py                   # Main Flask API
│   ├── requirements.txt         # Python dependencies
│   └── README.md                # Backend setup guide
│
├── frontend/                    # React frontend
│   ├── src/
│   │   └── components/
│   │       └── DashboardChart.js
│   ├── package.json
│   └── README.md                # Frontend setup guide
│
├── docs/                        # Screenshots & API examples
│   ├── screenshots/
│   └── api-guide.md
│
└── README.md                    # Main documentation (this file)
⚙️ Setup Instructions
🐍 Backend Setup (Flask)

Copy code
cd backend
pip install -r requirements.txt
python app.py
By default, your backend runs at:
👉 http://localhost:5000/api/dashboard

Your local MongoDB instance should be running at:

Copy code
mongodb://localhost:27017
Database: Finacial_dashboard
Collection: metrics

⚛️ Frontend Setup (React)
bash
Copy code
cd frontend
npm install
npm start
Then open your browser at:
👉 http://localhost:3000

The dashboard will automatically fetch data from:
http://localhost:5000/api/dashboard

🔗 API Reference (Local MongoDB)
Method	Endpoint	Description
GET	/api/dashboard	Fetch latest dashboard for frontend
GET	/api/dashboards	Fetch all dashboard documents
POST	/api/dashboard/	Create a new dashboard entry
PUT	/api/dashboard/<id>	Update a specific dashboard by ObjectId
DELETE	/api/dashboard/<id>	Delete a specific dashboard by ObjectId

🧪 Postman Examples
1️⃣ Create Data (POST)
URL: http://localhost:5000/api/dashboard/
Body (JSON):

json
Copy code
{
  "data": [1, 2, 3],
  "layout": { "title": "Test" }
}
2️⃣ View Latest Data (GET)
URL: http://localhost:5000/api/dashboard

3️⃣ Update Data (PUT)
URL:
http://127.0.0.1:5000/api/dashboard/68ee8cba52f5400824de5d5c
Body (JSON):

json
Copy code
{
  "data": [4, 5, 8],
  "layout": { "title": "ja Test" }
}
4️⃣ Delete Data (DELETE)
URL:
http://127.0.0.1:5000/api/dashboard/68ee8cba52f5400824de5d5c

5️⃣ View All Dashboards (GET)
URL: http://localhost:5000/api/dashboards

🧭 Future Enhancements
🚀 Add support for multiple charts or dashboards
📊 Connect MongoDB Atlas for cloud storage
🧰 Add UI filters for different date ranges and KPIs

💬 Collaboration & Feedback
👥 All contributors (developers, analysts) can:

Comment or open GitHub Issues for suggestions

Use the docs/ folder for visuals and sample data


👩‍💻 Author
Madhuri Patidar
💼 Full Stack Developer (Java | React | Python | MongoDB)
💬 “Always learning, building, and sharing.”

📄 License

MIT License © 2025 Madhuri Patidar
