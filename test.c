#include <stdio.h>
#include <stdlib.h>
#include "rsa.c"

int main(void)
{
    for (int i = 234; i < 244; i++)
    {
        BIGINT left = randrange(234224342,238492348234);
        BIGINT right = randrange(132321,234423423);
        BIGINT mod= randrange(132132,342324324);
        BIGINT num1 = modulo(left, right, mod);
        printf("Iteration %d\n", i);
    }
}