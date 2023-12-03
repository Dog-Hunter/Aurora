import socket


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

class ServerConnection(Connection):
    def __init__(self, host='127.0.0.1', port=32000):
        super().__init__(host, port)

    def create_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)

class ClientConnection(Connection):
    def __init__(self, host, port=32000):
        super().__init__(host, port)

    def create_client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))