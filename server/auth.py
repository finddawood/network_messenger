from network_messenger.shared.protocol_constants import OK, ERROR

def handle_auth(db, command, payload):
    username, password = payload.split(":")
    if command == "REGISTER":
        return OK if db.register(username, password) else ERROR
    if command == "LOGIN":
        return OK if db.authenticate(username, password) else ERROR
