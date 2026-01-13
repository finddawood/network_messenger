from network_messenger.server.protocol import recv_packet
from network_messenger.shared.protocol_constants import MSG, FILE


def receive(sock):
    while True:
        cmd, payload = recv_packet(sock)
        if cmd == MSG:
            print("Message:", payload.decode())
        elif cmd == FILE:
            with open("received_file", "wb") as f:
                f.write(payload)
            print("File received")
