'''
Creates client and server
'''

from cgi import test
import socket
import pickle

SERVER_PORT = 63527
CLIENT_PORT = 35452
RECV_SIZE = 2**200

class BaseSocket:
    "The base for the client and server sockets"
    def __init__(self, addr, port) -> None:
        self.socket = socket.socket()
        self.addr = addr
        self.port = port
        self.self_ip = (self.addr, self.port)
        self.socket.bind(self.self_ip)
        self.socket.settimeout(3)

    def encode(self, data: str) -> bytes:
        "Encoding function"
        encoded = pickle.dumps(data)
        return encoded

    def decode(self, data: bytes) -> str:
        "Decoding function"
        decoded = pickle.loads(data)
        return decoded

    def send(self, data):
        "Sends data"
        self.socket.send(self.encode(data))

    def recv(self):
        "Receives data"
        data = self.decode(self.socket.recv(RECV_SIZE))

        print(f"Received {data}")
        return data

    def close(self):
        "Closes the socket"
        self.socket.close()
        print("Closed socket")

class ClientSocket(BaseSocket):
    "The client socket"
    def __init__(self, addr="0.0.0.0") -> None:
        # Gets the base elements
        super().__init__(addr, CLIENT_PORT)
        self.socket.settimeout(10)
        self.server = ()
    def connect(self, server) -> None:
        "Connects to server"
        self.server = (server, SERVER_PORT)
        try:
            self.socket.connect(self.server)
        except ConnectionRefusedError:
            print("Connection Refused. Trying again")
            self.connect(self.server)

class ServerSocket(BaseSocket):
    "The server socket"
    def __init__(self) -> None:
        # Maybe change to get_ip if this doesn't work
        super().__init__("0.0.0.0", SERVER_PORT)
        self.conn = ""

        print("ServerSocket Called!")
        self.socket.listen(5)

    def listen(self) -> None:
        "Listens for connection"
        try:
            self.conn, self.return_addr = self.socket.accept()
        except socket.timeout:
            print("Timed out. Trying again")
            self.listen()
        print("Connected by", self.return_addr)
