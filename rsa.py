from random import randint
import subprocess
import sys
from time import sleep
import warnings
import prime


def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)
    
class RSAKey:
    def __init__(self, create_key=False):
        if create_key:
            p = prime.getPrime()
            q = prime.getPrime()
            self.n = p*q
            λ = (p-1)*(q-1)
            self.e = 65537
            self.d = pow(self.e, -1, λ)
        self.target = RSADummy

    def encode(self, text: str):
        if not self.target.e and not self.target.n:
            print()
            sys.exit(2)

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

def main():
    alice = RSAKey(create_key=True)
    bob = RSAKey()


    bob.target.n = alice.n
    bob.target.e = alice.e

    text1 = bob.encode("convallis tellus id interdum velit laoreet id donec ultrices tincidunt arcu non sodales neque sodales ut etiam sit amet nisl purus in mollis nunc sed id semper risus in hendrerit gravida rutrum quisque non tellus orci ac auctor augue mauris")
    text2 = bob.encode("Hello!")


    print(f"Encoded texts: {text1}, {text2}")

    uncoded1 = alice.decode(text1)
    uncoded2 = alice.decode(text2)
    print(uncoded1, uncoded2)

if __name__ == "__main__":
    main()

