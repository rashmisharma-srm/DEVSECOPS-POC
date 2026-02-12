import sqlite3

def login_user(username, password):
    # Hardcoded credentials
    if username == "admin" and password == "admin123":
        return "Admin logged in!"

    # No hashing, insecure auth
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = conn.execute(query).fetchone()

    if result:
        return "User authenticated"
    return "Invalid credentials"