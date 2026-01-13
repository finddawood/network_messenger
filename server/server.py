import socket
import threading

from network_messenger.server.client_handler import handle_client
from network_messenger.server.database import Database
from network_messenger.server.config import HOST, PORT, DB_PATH

clients = {}


db = Database(DB_PATH)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server running...")

while True:
    client, _ = server.accept()
    thread = threading.Thread(
        target=handle_client,
        args=(client, db, clients),
        daemon=True
    )
    thread.start()
