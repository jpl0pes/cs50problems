#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <math.h>
#include <ctype.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26*26;

// Hash table
node *table[N];
int count_words;

int main(void)
{
    // Loads dictionary into memory, returning true if successful else false
    //bool load(const char *dictionary)
    FILE *dictionary = fopen("dictionaries/small","r");
    if (dictionary == NULL)
    {
        printf("there is no godamn dictionary!\n");
        return 1;
    }

    printf("Dictionary is open for business\n");

    char tmpwords[LENGTH + 1];
    node *n = NULL;

    while (fscanf(dictionary, "%s", tmpwords) != EOF)
    {
        int hash_value = hash(tmpwords);

        if (table[hash_value] == NULL)
        {
            n = malloc(sizeof(node));
            if (n == NULL)
            {
                printf("Ran out of memory m8");
                return 1;
            }

            for (int i = 0; i < strlen(tmpwords); i++)
            {
                n->word[i] = tmpwords[i];
            }

            //Define where are the nodes pointing. The head points to node and node to NULL
            table[hash_value] = n;
            n->next = NULL;
            count_words++;

        }
        else
        {
            n = malloc(sizeof(node));
            if (n == NULL)
            {
                printf("Ran out of memory m8");
                return 1;
            }

            for (int i = 0; i < strlen(tmpwords); i++)
            {
                n->word[i] = tmpwords[i];
            }

            //Define where are the nodes pointing. The new node points to last node and the list points to the new node
            n->next = table[hash_value];
            table[hash(n->word)] = n;
            count_words++;

        }

    }

    //Testing if things work

    for (int i = 0; i < N; i++)
    {
        for (node *tmp = table[i]; tmp != NULL; tmp = tmp->next)
        {
            // Within the node, we'll just print the number stored:
            printf("head_value:%i\tword:%s\n", i,  tmp->word);
        }
    }

    int y = size();
    printf("%i\n", y);

    bool z = check("charlie");
    if (z== true)
    {
        printf("Check....it exists\n");
    }
    else
    {
        printf("Check...dosen't eixist\n");
    }

    bool unloaded = unload();
    if (!unloaded)
    {
        printf("Could not unload\n");
        return 1;
    }



    // TODO
    return false;

}

unsigned int hash(const char *word)
{
    //For the alphabeitcal hash this thing needs to return a number from zero to 25 based on first letter
    //printf("%c\n",word[0]);
    int x = (word[0] + word[1]) % N;
    //printf("%i\n",x);
    return x;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return count_words  ;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int x = hash(word);
    for (node *tmp = table[x]; tmp != NULL; tmp = tmp->next)
    {
        int result = strcasecmp(word,tmp->word);
        if (result == 0)
        {
            return true;
            break;
        }
    }
    return false;

}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        if(table[i] != NULL)
        {
            node *tmp = NULL;
            for (node *cursor = table[i]; cursor != NULL ; cursor = cursor->next)
            {
                 if (tmp != NULL)
                {
                    free(tmp);
                }
                //printf("%s\n",cursor->word);
                tmp = cursor;
                free(tmp);
            }

        }
    }
return true;

}