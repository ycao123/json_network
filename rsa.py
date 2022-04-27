from random import randint
import subprocess
import sys
from time import sleep
import warnings


def generateLargePrime():
    number = randint(57, 60)
    sleep(0.1)
    prime = subprocess.getoutput(f"./rsa {number}")
    return int(prime)

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)
    
class RSAKey:
    def __init__(self, create_key=False):
        if create_key:
            p = generateLargePrime()
            q = generateLargePrime()
            self.n = p*q
            λ = (p-1)*(q-1)
            self.e = 65537
            self.d = pow(self.e, -1, λ)
        self.target = RSADummy

    def encode(self, text: str):
        m = self._encode(text)
        if m >= self.target.n:
            print("INVALID LENGTH")
            sys.exit(1)
        
        c = str(hex(pow(m, self.target.e, self.target.n))).encode()
        return c

    def decode(self, c):
        text = pow(int(c.decode(), 16), self.d, self.n)
        m = self._decode(text)
        return m

    def _decode(self, c):
        c = str(c)
        new_string = [c[i:i+2] for i in range(0, len(c), 2)]
        for i in range(len(new_string)):
            ascii_char = chr(int(new_string[i]) + 12)
            new_string[i] = ascii_char
        return "".join(new_string)




    def _encode(self, text: str):
        text = list(text)
        for i in range(len(text)):
            if (text[i] == ("{" or "|" or "}" or "~")):
                print("INVALID SYMBOLS")
                sys.exit(3)
            text[i] = ord(text[i].upper()) - 12
            text[i] = str(text[i])

        text = "".join(text)
        text = int(text)
        return text

    def modpow(self, b, e, m):
        if m == 1:
            return 0
        result = 1
        b = b % m
        while (e > 0):
            if (e % 2  == 1):
                result = (result * b) % m
            e >>= 1
            b = pow(b, 2, m)
        return result


    def __str__(self):
        return "A RSA Key for decryption and encryption uses"

class RSADummy(RSAKey):
    def __init__(self):
        self.n = None
        self.e = None

alice = RSAKey(create_key=True)
bob = RSAKey()


bob.target.n = alice.n
bob.target.e = alice.e

text = bob.encode("Some random text that")

print(f"Encoded text: {text}")

uncoded = alice.decode(text)
print(uncoded)

