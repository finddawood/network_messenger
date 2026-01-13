from network_messenger.server.protocol import send_packet
from network_messenger.shared.protocol_constants import MSG, FILE


def send_message(sock, text):
    send_packet(sock, MSG, text.encode())

def send_file(sock, path):
    with open(path, "rb") as f:
        send_packet(sock, FILE, f.read())
