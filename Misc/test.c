#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    int nondigitcounter = 0;
    for (int i = 0; i < strlen(argv[1]); i++)
    {
       if(isdigit(argv[1][i]) == false)
       {
           nondigitcounter++;
           //printf("%c %i\n", argv[1][i], nondigitcounter);
       }
       else
       {

       }
    }
    if (nondigitcounter == 0)
    {
        printf("%i\n", nondigitcounter);
        return true;
    }
    else
    {
        printf("%i\n", nondigitcounter);
        return false;
    }

}