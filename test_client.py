from base_socket import ClientSocket as CSocket

test_socket = CSocket()

test_socket.connect("0.0.0.0")
print(test_socket.recv())
test_socket.send("Goodbye!")