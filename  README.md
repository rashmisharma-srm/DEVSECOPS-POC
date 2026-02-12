from flask import Flask, request
import sqlite3
import subprocess
from utils import insecure_hash

app = Flask(__name__)

@app.route("/user")
def get_user():
    username = request.args.get("username")

    # Vulnerable to SQL Injection
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username='{username}'"
    result = conn.execute(query).fetchall()
    return str(result)

@app.route("/ping")
def ping():
    ip = request.args.get("ip")

    # RCE Vulnerability
    output = subprocess.check_output(f"ping -c 1 {ip}", shell=True)
    return output.decode()

@app.route("/hash")
def hash_api():
    password = request.args.get("password")

    # Weak hashing
    return insecure_hash(password)

if __name__ == "__main__":
    app.run(debug=True)