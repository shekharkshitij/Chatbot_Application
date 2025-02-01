import sqlite3

def create_connection():
    """Establish and return a connection to the SQLite database."""
    return sqlite3.connect("users.db")

def create_tables():
    """Create the users table if it does not exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mobile TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
