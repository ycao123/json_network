from client_socket import ClientSocket as CSocket
import unittest

test_socket = CSocket()
    
class TestClient(unittest.TestCase):
    def test_bool(self):
        self.assertEqual(True, False)


if __name__ == "__main__":
    unittest.main()