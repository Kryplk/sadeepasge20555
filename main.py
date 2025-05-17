from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your Supabase info
SUPABASE_URL = "https://xigrwvmqzdkfknxzlmxl.supabase.co"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhpZ3J3dm1xemRrZmtueHpsbXhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc0ODgwMjAsImV4cCI6MjA2MzA2NDAyMH0.7dKBFCqOURmL2tp92hkfK1iGwhAvl6UfOzsYwe5GVj0"
SUPABASE_TABLE = "users"

@app.route("/", methods=["GET"])
def index():
    return "API is working."

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"success": False, "message": "Missing credentials"}), 400

    headers = {
        "apikey": SUPABASE_API_KEY,
        "Authorization": f"Bearer {SUPABASE_API_KEY}",
        "Content-Type": "application/json",
    }

    filter_url = f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?username=eq.{username}&password=eq.{password}&select=*"
    response = requests.get(filter_url, headers=headers)

    if response.status_code != 200:
        return jsonify({"success": False, "message": "Supabase error"}), 500

    users = response.json()
    if users:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
