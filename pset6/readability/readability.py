import cs50


def main():
    ##Input String or Text
    text = str(input("Text: "))
    A = characters(text)
    B = words(text)
    C = sentences(text)
    ##print(A, B, C)

    avg_letters = float(A/B*100)
    avg_sentences = float(C/B*100)
    index = float(0.0588 * avg_letters - 0.296 * avg_sentences - 15.8)
    rounded_index = round(index)

    if (index < 1):
        print("Before Grade 1");
    elif (index > 16):
        print("Grade 16+");
    else:
        print("Grade: ", rounded_index);



##Count number of characters in string
def characters(text):
    counter_characters = 0

    for i in range(len(text)):
        if (text[i].isalpha() == True):
            counter_characters +=1
    ##print("Number of characters:", counter_characters)
    return counter_characters



##Count number of words

def words(text):
    counter_words = 1
    for i in range(len(text)):
        if (text[i] == " "):
            counter_words += 1
    ##print("Number of words:", counter_words)
    return counter_words

##Count number of sentences
def sentences(text):
    counter_sentences = 0
    for i in range(len(text)):
        if (text[i] == '.' or text[i] == '!' or text[i] == '?' ):
            counter_sentences += 1
    ##print("Number of sentences:", counter_sentences)
    return counter_sentences


main()