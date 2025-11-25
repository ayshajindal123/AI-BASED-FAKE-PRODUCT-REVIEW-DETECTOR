from flask import Blueprint, request, jsonify

auth = Blueprint("auth", __name__)

# Temporary user storage (memory only)
users = {}

@auth.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"success": False, "message": "Username already exists"})

    users[username] = password
    return jsonify({"success": True, "message": "Signup successful"})


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"success": False, "message": "User not found"})

    if users[username] != password:
        return jsonify({"success": False, "message": "Incorrect password"})

    return jsonify({"success": True, "message": "Login successful"})
