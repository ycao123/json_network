from lib2to3.pytree import Base
from base_socket import ClientSocket as CSocket
    
test_socket = CSocket()

try:
    test_socket.connect("0.0.0.0")
    test_socket.send("Goodbye!")
    print(test_socket.recv())

    test_socket.close()

except BaseException as error:
    print(error)
    test_socket.close()
    exit()