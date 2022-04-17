from random import randrange
from math import sqrt

SMALLEST = 10**300

LARGEST = int("9"*300)

class PrimeInt(int):
    pass

def Prime():
    randnum = randrange(SMALLEST, LARGEST)
    
    isPrime = False

    for i in range(2, int(sqrt(randnum)) + 1):
        if (randnum % i == 0):
            isPrime = True
            break
    if isPrime:
        return randnum
    else:
        Prime()

class RSAKey:
    pass

print(Prime())