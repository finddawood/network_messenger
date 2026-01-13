# 📡 Network Messenger

A Python-based client-server network messaging application designed to facilitate communication between multiple clients via a central server. This project includes separate modules for the client, server, shared utilities, and message storage, enabling structured and modular development of network messaging features.

---

## 📑 Table of Contents

- [About](#about)
- [Features](#features)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Server](#running-the-server)
  - [Running the Client](#running-the-client)
- [Example Workflow](#example-workflow)
- [Configuration](#configuration)
- [Dependencies](#dependencies)


---

## 📖 About

**Network Messenger** is an open-source Python networking application that provides a simple framework for real-time messaging between clients via a central server process. It is structured for easier understanding of socket programming, client-server communication, shared data formats, and message persistence.

This project targets developers and students interested in networking fundamentals and real-world usage of Python sockets and network protocols.

---

## ✨ Features

- **Client-Server Architecture:** Centralized message delivery and management
- **Multi-Client Support:** Multiple clients can connect simultaneously
- **Shared Protocol:** Common utilities for message formatting and handling
- **Persistent Storage:** Message history and data persistence via `storage/`
- **Activity Logging:** Server logs connections and activity to `server.log`
- **Modular Design:** Clean separation of concerns for easy extension
- **Real-Time Messaging:** Instant message delivery between connected clients

---

## 📁 Repository Structure

```text
.
├── client/                    # Client application logic
├── server/                    # Server implementation
├── shared/                    # Shared utilities and protocol definitions
├── storage/                   # Message persistence and data storage
├── __init__.py                # Root package initializer
├── req.txt                    # Python dependency list
├── server.log                 # Log file for server activity
└── README.md                  # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/finddawood/network_messenger.git
cd network_messenger
```

### 2. Set Up Python Environment

Python 3.8 or higher is recommended.

```bash
# Create virtual environment
python3 -m venv venv

# Activate on Linux/macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r req.txt
```

---

## 🚀 Usage

Before starting clients, you need to start the server.

### 🔹 Running the Server

```bash
python server/main.py
```

**This will:**
- Launch the messaging server
- Listen for incoming client connections
- Log activity to `server.log`

**Server Output Example:**
```
[INFO] Server started on 127.0.0.1:5000
[INFO] Waiting for connections...
[INFO] Client connected: 127.0.0.1:54321
```

### 🔹 Running the Client

In a separate terminal, start one or more clients:

```bash
python client/main.py
```

**Clients will:**
- Connect to the server
- Allow sending and receiving messages
- Use shared utilities for messaging protocol

**Client Interface Example:**
```
Connected to server at 127.0.0.1:5000
Enter message: Hello, World!
[Sent] Hello, World!
[Received] User2: Hi there!
```

---

## 🧠 Example Workflow

1. **Start the server** in one terminal:
   ```bash
   python server/main.py
   ```

2. **Open multiple client terminals** (e.g., 3 separate windows):
   ```bash
   # Terminal 1
   python client/main.py
   
   # Terminal 2
   python client/main.py
   
   # Terminal 3
   python client/main.py
   ```

3. **Send messages from any client** and observe delivery

4. **Check the logs** in `server.log` to see connection activity

### Example Interaction

```
Client 1: Hi everyone!
Client 2: Hello!
Client 3: Hey there!
```

All messages are routed through the server and delivered to connected clients.

---

## ⚙️ Configuration

You can configure server settings by modifying the configuration in `server/main.py` or creating a config file:

```python
HOST = '127.0.0.1'  # Server host
PORT = 5000         # Server port
MAX_CLIENTS = 10    # Maximum concurrent connections
```

---

## 📦 Dependencies

This project uses external Python packages listed in `req.txt`. Install them via:

```bash
pip install -r req.txt
```

**Common dependencies may include:**
- `socket` (built-in)
- `threading` (built-in)
- `logging` (built-in)
- Additional packages as needed for encryption, UI, etc.

---

## 🤝 Contributing

Contributions are welcome! Help improve Network Messenger by adding features, fixing bugs, or enhancing documentation.

### How to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/MessagingFeature`)
3. Commit your changes (`git commit -m 'Add some MessagingFeature'`)
4. Push to the branch (`git push origin feature/MessagingFeature`)
5. Open a Pull Request

### Ideas for Contributions

- Add user authentication
- Implement message encryption
- Create a GUI client
- Add private messaging
- Implement chat rooms
- Add file transfer support

