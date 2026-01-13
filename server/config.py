import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST = "127.0.0.1"
PORT = 5001
DB_PATH = os.path.join(BASE_DIR, "storage", "users.db")
