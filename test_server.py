from base_socket import ServerSocket as SSocket

test_socket = SSocket()
test_socket.listen()
test_socket.send("Hello!")

print(test_socket.recv())

test_socket.close()