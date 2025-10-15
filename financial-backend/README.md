
# 🐍 Financial Dashboard – Backend (Flask API)

The **backend** of the Financial Dashboard is a RESTful API built with **Flask** and connected to a **local MongoDB** database.  
It handles all CRUD operations for dashboard data that the React frontend visualizes.

---

## 🧠 Overview

This Flask API:
- Connects to a local MongoDB instance via PyMongo
- Exposes endpoints for Create, Read, Update, Delete
- Supports CORS for React frontend access
- Returns JSON data suitable for Plotly charts

---

## ⚙️ Setup Instructions

### Step 1: Install dependencies
```bash
cd backend
pip install -r requirements.txt
Step 2: Run the Flask server
bash
Copy code
python app.py
Your backend will run at:
👉 http://localhost:5000

## 🚀 Features
- API with Create, Read, Update, Delete (CRUD)
- Connects to MongoDB
- Tested with Postman

🗂️ Folder Structure

Copy code
backend/
│
├── app.py                # Main Flask API
├── requirements.txt      # Backend dependencies
└── README.md
🗃️ MongoDB Setup
Make sure MongoDB Compass or MongoDB service is running locally:


Copy code
mongodb://localhost:27017
Database: Finacial_dashboard
Collection: metrics

🔗 API Endpoints
Method	Endpoint	Description
GET	/api/dashboard	Fetch latest dashboard document
GET	/api/dashboards	Fetch all dashboard documents
POST	/api/dashboard/	Add new dashboard data
PUT	/api/dashboard/<id>	Update dashboard by ObjectId
DELETE	/api/dashboard/<id>	Delete dashboard by ObjectId

🧪 Example (Postman)
POST
URL: http://localhost:5000/api/dashboard/
Body (JSON):

json
Copy code
{
  "data": [1, 2, 3],
  "layout": { "title": "Test" }
}
GET
URL: http://localhost:5000/api/dashboard

PUT
URL: http://localhost:5000/api/dashboard/68ee8cba52f5400824de5d5c
Body (JSON):

json
Copy code
{
  "data": [4, 5, 8],
  "layout": { "title": "Ja Test" }
}
DELETE
URL: http://localhost:5000/api/dashboard/68ee8cba52f5400824de5d5c

🧭 Future Enhancements
Add authentication and API key access
Connect to MongoDB Atlas for cloud hosting

Tools
Flask, Flask-CORS, PyMongo

💬 Feedback
Ask questions in Issues!

Made with ❤️ by Madhuri Patidar
