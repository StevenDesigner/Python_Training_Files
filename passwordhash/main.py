from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Simulated "database" (in-memory dictionary)
users = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    if username in users:
        return jsonify({"message": "User already exists!"}), 400

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Store in "database"
    users[username] = hashed_password

    return jsonify({
        "message": f"User {username} registered successfully!",
        "stored_hash": hashed_password   # 👈 Just to show what is stored
    }), 201


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user_hash = users.get(username)

    if user_hash and check_password_hash(user_hash, password):
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid username or password"}), 401


@app.route('/users', methods=['GET'])
def list_users():
    """ For debugging only: shows all registered users and their hashes """
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
