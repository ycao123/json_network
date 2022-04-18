#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define BIGINT __uint128_t
#define bool int
#define true 0
#define false 1
#define ACCURACY 10

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

/* 
 * calculates (a ** b) % c. A pretty fast algorithm
 */
BIGINT modpow(BIGINT x, unsigned int y, BIGINT p)
{
    int res = 1;
    x = x % p;
    if (x == 0) return 0;
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
 
        // y must be even now
        y = y>>1;
        x = (x*x) % p;
    }
    return res;
}

bool rabinMiller(BIGINT n)
{
    BIGINT d = 0;
    BIGINT r = n - 1;
    while ((r&1) == 0)
    {
        d++;
        r>>1;
    }
 
    // Iterate given number of 'k' times
    for (int i = 0; i < ACCURACY; i++)
    {
        BIGINT a = randrange(2, n - 2);
        BIGINT x = modpow(a, d, n);
        if (x == 1 || x == n - 1)
        {
            continue;
        }

        bool test_passed = false;

        for (int i = 0; i < (r - 1); i++)
        {
            x = modpow(x, 2, n);
            if (x == 1)
            {
                return false;
            }
            if (x == n - 1)
            {
                test_passed = true;
                break;
            }
        }
        if (!test_passed)
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
            return true;
        }
        if (n % p == 0)
        {
            return false;
        }
    }
    return rabinMiller(n);
}

BIGINT randrange(BIGINT upper, BIGINT lower)
{
    BIGINT num = (arc4random() % (upper - lower + 1)) + lower;
    return num;
}

BIGINT generateLargePrime(int k)
{
    BIGINT n;
    for (;;)
    {
        BIGINT lower = pow(2, k - 1) + 1;
        BIGINT upper = pow(2, k) - 1;
        n = randrange(upper, lower);
        bool is_it_prime = isPrime(n);
        if (is_it_prime)
        {
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
    BIGINT num1 = generateLargePrime(128);
    printf("%llu\n", num1);
}