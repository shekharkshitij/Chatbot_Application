import hashlib
import sqlite3  # Ensure this is imported
from utils.database import create_connection

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(name, email, mobile, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, mobile, password) VALUES (?, ?, ?, ?)",
                       (name, email, mobile, hash_password(password)))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:  # This requires sqlite3 to be imported
        conn.close()
        return False

def authenticate_user(email, password):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    return user
