from flask import Flask, request
import sqlite3
import subprocess
from utils import insecure_hash
from insecure_auth import login_user
from file_uploads import save_user_file
from crypto_issues import decrypt_sensitive_data

app = Flask(__name__)

@app.route("/user")
def get_user():
    username = request.args.get("username")

    # SQL Injection
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username='{username}'"
    result = conn.execute(query).fetchall()
    return str(result)

@app.route("/ping")
def ping():
    ip = request.args.get("ip")

    # Remote Command Execution
    output = subprocess.check_output(f"ping -c 1 {ip}", shell=True)
    return output.decode()

@app.route("/login", methods=["POST"])
def login():
    return login_user(request.form.get("username"), request.form.get("password"))

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    return save_user_file(file)

@app.route("/decrypt")
def decrypt():
    encrypted_data = request.args.get("data")
    return decrypt_sensitive_data(encrypted_data)

@app.route("/hash")
def hash_api():
    password = request.args.get("password")
    return insecure_hash(password)

if __name__ == "__main__":
    app.run(debug=True)