import sqlite3

class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
        """)
        self.conn.commit()

    def register(self, username, password):
        try:
            self.conn.execute("INSERT INTO users VALUES (?,?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def authenticate(self, username, password):
        cur = self.conn.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )
        return cur.fetchone() is not None
