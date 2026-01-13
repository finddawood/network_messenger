import socket
import threading

from network_messenger.client.config import SERVER_HOST, SERVER_PORT
from network_messenger.client.receiver import receive
from network_messenger.client.sender import send_message, send_file
from network_messenger.shared.protocol_constants import MSG, FILE, LOGIN, REGISTER
from network_messenger.server.protocol import send_packet



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_HOST, SERVER_PORT))

choice = input("login/register: ")
user = input("username: ")
pwd = input("password: ")

send_packet(sock, choice.upper(), f"{user}:{pwd}".encode())
threading.Thread(target=receive, args=(sock,), daemon=True).start()

while True:
    cmd = input("msg/file: ")
    if cmd == "msg":
        send_message(sock, input("text: "))
    elif cmd == "file":
        send_file(sock, input("path: "))
