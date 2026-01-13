def recv_line(sock):
    data = b""
    while not data.endswith(b"\n"):
        chunk = sock.recv(1)
        if not chunk:
            return None
        data += chunk
    return data.decode().strip()


def recv_packet(sock):
    header = recv_line(sock)
    if not header:
        return None, None

    try:
        command, length = header.split("|")
        length = int(length)
    except ValueError:
        return None, None

    payload = b""
    while len(payload) < length:
        payload += sock.recv(length - len(payload))

    return command, payload


def send_packet(sock, command, payload=b""):
    header = f"{command}|{len(payload)}\n".encode()
    sock.sendall(header)
    if payload:
        sock.sendall(payload)
