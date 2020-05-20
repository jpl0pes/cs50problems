//includes
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>


//functions
int letters(string a);
int words(string b);
int sentences(string c);

int main(void)
{
    //something to get the string from the user
    string text = get_string("What's the text we're evaluating?: ");

    //count within the string the letters. I need to cycle through the array and add 1 everytime it accounters a letter or a symbol
    int number_letters = letters(text);
    //printf("%i letter(s)\n", number_letters);

    //count within the string the words. I maybe could get away with counting spaces here
    int number_words = words(text);
    //printf("%i word(s)\n", number_words);

    //count within the string how many setences. I need to find the . or !
    int number_sentences = sentences(text);
    //printf("%i sentence(s)\n", number_sentences);

    //Return the index
    float L = (float)number_letters / number_words  * 100;
    float S = (float)number_sentences / number_words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int rounded_index = round(index);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", rounded_index);
    }



}

//Function of Letters

int letters(string a)
{
    int letters = 0;
    for (int i = 0; a[i] != '\0'; i++)
    {
        if (isalpha(a[i]))
        {
            letters = letters + 1;
            //printf("Character ASCII %i i Value %i Letters %i\n", a[i], i, letters);
        }

    }
    return letters;
}

//Function of Words

int words(string b)
{
    int words = 1;
    for (int i = 0; b[i] != '\0'; i++)
    {
        if (isspace(b[i]))
        {
            words = words + 1;
               //printf("Value %i number of words %i\n", i, words);
        }
    }
    return words;
}

//Function of Sentences

int sentences(string c)
{
    int sentences = 0;
    for (int i = 0; c[i] != '\0'; i++)
    {
        if (c[i] == '.' || c[i] == '!' || c[i] == '?' )
        {
            sentences = sentences + 1;
            //printf("Value %i numner of sentences %i\n", i, sentences);
        }
    }
    return sentences;
}