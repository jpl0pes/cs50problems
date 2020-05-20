//includes
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>

//functions


//Main Function
int main(int argc, string argv[])
{
    //check if there are any non digits in the argv
     if (argc != 2)
    {
       printf("Usage ./caesar key\n");
       return 1;
    }
    else
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
    //Muleta: printf("nondigit counter %i\n", nondigitcounter);

    //check if argc count is different than 2 and if nondigit is false
    if (argc != 2 || nondigitcounter != 0)
    {
        printf("Usage ./caesar key\n");
        return 1;

    }
        else
        {

        }
        //convert the key to an integer. atoi is a function that does this
        int key = atoi(argv[1]);

        //get string as plaintext
        string plaintext = get_string("plaintext: ");

        //declare cyphertext
        char cyphertext[strlen(plaintext)-1];

        //replace each letter of cyphertext by plaintext following the key
        for (int j = 0; plaintext[j] != '\0'; j++)
        {
            //if the character is alphabetical do this if not maintain the character
            if (isalpha(plaintext[j]))
            {
                //See if the character is upper or lower so you can convert to the right place in the alphabet
                if( islower(plaintext[j]))
                {
                    cyphertext[j] = (plaintext[j] + key - 'a') % 26 + 'a';
                }
                else
                {
                    cyphertext[j] = (plaintext[j] + key - 'A') % 26 + 'A';
                }
            }
            else
            {
                cyphertext[j] = plaintext[j];
            }
        }
        //print Cyphertext
        printf("ciphertext: %s\n", cyphertext);

    }
}



