from base_socket import BaseSocket, SERVER_PORT
import sys
import random
from rsa import RSAKey

class ClientSocket(BaseSocket):
    "The client socket"
    def __init__(self, addr="0.0.0.0") -> None:
        'Get the base elements for the socket'
        super().__init__(addr, random.randint(23535, 52949))
        self.socket.settimeout(10)
        self.server = ()
        self.rsa = RSAKey(create_key=True)

    def encode(self, text):
        return self.rsa.encode(text)

    
    def connect(self, server) -> None:
        "Connects to server"
        self.server = (server, SERVER_PORT)
        try:
            self.socket.connect(self.server)
        except ConnectionRefusedError:
            print("Connection Refused. Server might not be open. Try checking your IPv4")
            self.socket.close()
            sys.exit()