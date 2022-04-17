from base_socket import ServerSocket as SSocket


test_socket = SSocket()
try:
    test_socket.listen()

    print(test_socket.recv())

    test_socket.send("Hello!")

except BaseException as error:
    print(error)
    test_socket.close()
    exit()
