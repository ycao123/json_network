#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <inttypes.h>

#define BIGINT __uint64_t
#define bool int
#define true 0
#define false 1
#define ACCURACY 10
#define _PBIGINT PRIu64

int lowPrimes[] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
                   ,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179
                   ,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269
                   ,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367
                   ,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461
                   ,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571
                   ,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661
                   ,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773
                   ,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883
                   ,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997};

BIGINT randrange(BIGINT upper, BIGINT lower);

BIGINT mulmod(BIGINT a, BIGINT b, BIGINT mod)
{
    BIGINT x = 0,y = a % mod;
    while (b > 0)
    {
        if (b % 2 == 1)
        {    
            x = (x + y) % mod;
        }
        y = (y * 2) % mod;
        b /= 2;
    }
    return x % mod;
}
/* 
 * modular exponentiation
 */
BIGINT modulo(BIGINT base, BIGINT exponent, BIGINT mod)
{
    BIGINT x = 1;
    BIGINT y = base;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) % mod;
        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}
 
/*
 * Miller-Rabin Primality test, iteration signifies the accuracy
 */
int Miller(BIGINT p,int iteration)
{
 
    int i;
    BIGINT s;
    if (p < 2)
    {
        return false;
    }
    if (p != 2 && p % 2 == 0)
    {
        return false;
    }
    s = p - 1;
    while (s % 2 == 0)
    {
        s /= 2;
    }

    for (i = 0; i < iteration; i++)
    {
        BIGINT a = arc4random() % (p - 1) + 1, temp = s;
        BIGINT mod = modulo(a, temp, p);
        while (temp != p - 1 && mod != 1 && mod != p - 1)
        {
            mod = mulmod(mod, mod, p);
            temp *= 2;
        }
        if (mod != p - 1 && temp % 2 == 0)
        {
            return false;
        }
    }
    return true;
}


bool isPrime(BIGINT n)
{
    for (int i = 0; i < 167; i++)
    {
        int p = lowPrimes[i];
        if (n == p)
        {
            printf("Found a low prime");
            return true;
        }
        if (n % p == 0)
        {
            return false;
        }
    }
    return Miller(n, ACCURACY);
}

BIGINT randrange(BIGINT upper, BIGINT lower)
{
    BIGINT num = (arc4random() % (upper - lower + 1)) + lower;
    return num;
}

BIGINT generateLargePrime(int k)
{
    BIGINT n;
    BIGINT lower = pow(2, k - 1) + 1;
    BIGINT upper = pow(2, k) - 1;
    for (;;)
    {
        n = randrange(upper, lower);
        bool check = isPrime(n);
        if (check == true)
        {
            printf("It is prime!\n");
            break;
        }
        else
        {
            continue;
        }
    }
    return n;
}

int main(void)
{
    BIGINT num1 = generateLargePrime(64);
    printf("%"_PBIGINT"\n", num1);
}