from network_messenger.server.protocol import recv_packet, send_packet
from network_messenger.server.logger import logger
from network_messenger.server.auth import handle_auth
from network_messenger.shared.protocol_constants import MSG, FILE, OK, ERROR



def handle_client(client, db, clients):
    user = None
    try:
        while True:
            command, payload = recv_packet(client)
            if not command:
                break

            if command in ["LOGIN", "REGISTER"]:
                response = handle_auth(db, command, payload.decode())
                send_packet(client, response.encode())
                if response == OK:
                    user = payload.decode().split(":")[0]
                    clients[user] = client

            elif command == MSG:
                message = payload.decode()
                for u, sock in clients.items():
                    if sock != client:
                        send_packet(sock, MSG, message.encode())

            elif command == FILE:
                for sock in clients.values():
                    if sock != client:
                        send_packet(sock, FILE, payload)

    except Exception as e:
        logger.error(str(e))
    finally:
        if user in clients:
            del clients[user]
        client.close()
