from flask import Flask, request, jsonify

app = Flask(__name__)

# In real deployment, replace this with a proper DB connection or a persistent store
# For now, a simple in-memory user list:
users = {
    "user1": "pass1",
    "user2": "pass2",
    # add more users here
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        return jsonify({"success": True, "message": "Login successful"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
