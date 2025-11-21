import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

# Allow your React app (adjust if you use other origins)
CORS(app, origins=["http://localhost:3000", "https://financial-dashboard-project-eta.vercel.app"])

MONGO_URI = os.getenv("MONGO_URI", "")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI not set in environment")

client = MongoClient(MONGO_URI)
db = client["financial_dashboard"]
charts_collection = db["charts"]

@app.route("/")
def home():
    return jsonify({"message": "Financial Dashboard API - LIVE", "charts_endpoint": "/api/charts"})

def _matches_quarter_in_name(name: str, quarter_lower: str) -> bool:
    if not name or not isinstance(name, str):
        return False
    nl = name.lower()
    return quarter_lower in nl

@app.route('/api/charts', methods=['GET'])
def get_charts():
    """
    Returns charts from db.charts.
    Optional query params:
      - quarter=<YYYY-Qn>  (e.g. 2018-Q4)  OR quarter=median
      - company=<partialName>  (optional, case-insensitive substring match in trace.name)
    Behavior:
      - If quarter provided: each chart.data is filtered for traces whose name contains the quarter text
        (or 'median' when quarter=median).
      - For chart index 3 (4th chart), layout.title text is updated to include the quarter label.
      - Keeps dropdown menu intact in 4th chart for quarter selection.
    """
    try:
        quarter = (request.args.get("quarter") or "").strip()
        company = (request.args.get("company") or "").strip().lower()

        quarter_lower = quarter.lower()
        use_quarter = bool(quarter)
        use_median = quarter_lower == "median"

        cursor = charts_collection.find().sort("_id", 1)
        charts = {}
        for idx, doc in enumerate(cursor):
            layout = dict(doc.get("layout", {})) if isinstance(doc.get("layout", {}), dict) else doc.get("layout", {})
            config = dict(doc.get("config", {})) if isinstance(doc.get("config", {}), dict) else doc.get("config", {})
            orig_traces = list(doc.get("data", []))

            filtered_traces = orig_traces

            if company:
                filtered_traces = [
                    tr for tr in filtered_traces
                    if tr.get("name") and company in tr.get("name", "").lower()
                ]

            if use_quarter:
                if use_median:
                    filtered_traces = [
                        tr for tr in filtered_traces
                        if tr.get("name") and "median" in tr.get("name", "").lower()
                    ]
                else:
                    q = quarter_lower
                    filtered_traces = [
                        tr for tr in filtered_traces
                        if tr.get("name") and q in tr.get("name", "").lower()
                    ]

            if idx == 3:
                # Update title dynamically based on quarter or median
                if use_quarter:
                    if use_median:
                        new_title = "Debt vs Liquid Assets: Median Across Quarters"
                    else:
                        new_title = f"Debt vs Liquid Assets: {quarter}"
                else:
                    new_title = "Debt vs Liquid Assets"

                if isinstance(layout, dict):
                    if isinstance(layout.get("title"), dict):
                        layout["title"]["text"] = new_title
                    else:
                        layout["title"] = {"text": new_title}
                else:
                    layout = {"title": {"text": new_title}}

            charts[f"chart{idx}"] = {
                "data": filtered_traces,
                "layout": layout,
                "config": config
            }

        return jsonify(charts)

    except Exception as e:
        app.logger.exception("Error in /api/charts")
        return jsonify({"error": str(e)}), 500

@app.route("/health")
def health():
    try:
        count = charts_collection.count_documents({})
    except Exception:
        count = 0
    return jsonify({"status": "OK", "db": "Connected", "charts_count": count})

if __name__ == "__main__":
    print("Starting Flask backend on http://localhost:5000")
    app.run(debug=True, port=5000)
