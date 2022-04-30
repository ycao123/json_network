from base_socket import BaseSocket, SERVER_PORT
import socket
import sys

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