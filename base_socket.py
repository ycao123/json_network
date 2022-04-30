'''
Creates client and server
'''

import socket
import pickle
import sys
from time import sleep as wait

SERVER_PORT = 63524
RECV_SIZE = 4096

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
        data = self.encode(data)
        self.socket.send(self.encode(data))
        print(f"Sent {data}")

    def recv(self):
        "Receives data"
        while True:
            try:
                data = self.socket.recv(RECV_SIZE)
                print("Received data")
                if not data:
                    break
                else:
                    data = self.decode(data)
            except socket.timeout:
                wait(0.1)

        if data == "SIGCLOSE":
            print("Received SIGCLOSE signal")
            self.socket.close()

        print(f"Received {data}")
        return data

    def close(self):
        "Closes the socket"
        self.send("SIGCLOSE")
        self.socket.close()
        print("Closed socket")


