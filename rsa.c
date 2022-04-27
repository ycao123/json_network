#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <inttypes.h>

#define BIGINT __uint64_t
#define bool int
#define true 0
#define false 1
#define ACCURACY 20
#define _PBIGINT PRIu64
#define ARRAY_SIZE 100

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
bool MillerRabin(BIGINT n);

BIGINT _power(BIGINT a,BIGINT b,BIGINT mod)
{
    if (a == 0 || b < mod / a)
        return (a*b)%mod;
    BIGINT sum;
    sum = 0;
    while(b>0)
    {
        if(b&1)
            sum = (sum + a) % mod;
        a = (2*a) % mod;
        b>>=1;
    }

    return sum;
}

BIGINT power(BIGINT x, BIGINT y, BIGINT p)
{
    BIGINT res = 1;     // Initialize result
 
    x = x % p; // Update x if it is more than or
                // equal to p
  
    if (x == 0) return 0; // In case x is divisible by p;
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y % 2 == 1)
            res = _power(res, x, p);
 
        // y must be even now
        y = y>>1; // y = y/2
        x = _power(x, x, p);
    }
    return res;
}

bool Fermat(BIGINT n)
{
    BIGINT result = power(2, n - 1, n);
    if (result == 1)
    {
        return MillerRabin(n);
    }
    else
    {
        return false;
    }
}

bool MillerRabin(BIGINT n)
{
    BIGINT s = 0;
    BIGINT q;
    BIGINT counter = n - 1;

    while (counter % 2 == 0)
    {
        s++;
        counter /= 2;
    }

    q = (n-1)/pow(2, s);

    for (int i = 0; i < ACCURACY; i++)
    {
        BIGINT a = randrange(1, n - 1);
        
        if (power(a, q, n) == 1)
        {
            return true;
        }
        else
        {
            for (int j = 0; j < s; j++)
            {
                if (power(a, (pow(2, i)* q), n) == n-1)
                {
                    return true;
                }
            }
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
    return Fermat(n);
}

BIGINT randrange(BIGINT upper, BIGINT lower)
{
    BIGINT num = (rand() % (upper - lower + 1)) + lower;
    return num;
}

BIGINT generateLargePrime(int k)
{
    BIGINT n = 0;
    BIGINT lower = pow(2, k - 1) + 1;
    BIGINT upper = pow(2, k) - 1;
    BIGINT range = upper - lower;
    for (;;)
    {
        n = randrange(upper, lower);
        bool check = isPrime(n);
        if (check == true) break;
    }
    return n;
}

int main(int argc, char* argv[])
{
    srand(time(NULL));
    if (argc == 1)
    {
        printf("Invalid Arguments");
        return 1;
    }
    for (int i = 1; i < argc; i++)
    {
        char* number_str = argv[i];
        int number_int = atoi(number_str);
        if (number_int == 1)
        {
            printf("Number cannot be 1\n");
            return 2;
        }
        BIGINT num1 = generateLargePrime(number_int);
        printf("%"_PBIGINT"\n", num1);
    }
}