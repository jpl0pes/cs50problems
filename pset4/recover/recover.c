#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    //Open a file
    FILE *file = fopen(argv[1], "r");

    //Check if it's a file
    if (!file)
    {
        return 1;
        exit(1);
    }

     //Check if input was given for argv
    if (argc != 2)
    {
        printf("Usage ./recover filename\n");
        return 1;
    }

    //Define variables
    unsigned char bytes[512];
    FILE *image = NULL;
    char filename[8];
    int jpeg_counter = 0;

    // Loop and read the bytes until the function returns less than SOMETHING
    // When you're fread it will automatically move where the file is going to be read afterwards. It's like an automatic loop through the file.
    //so when you make a condition based on fread it's not static, it will dynamically change everytime you call fread (it will return different values)
    while (fread(bytes, 512, 1, file) == 1)
    {
        //Condition if it's a JPEG
        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
    {
        if (image != NULL)
        {
            fclose(image);
        }

        sprintf(filename, "%03i.jpg", jpeg_counter);
        image = fopen(filename,"w");
        fwrite(bytes, 512, 1, image);
        jpeg_counter++;
    }
    else
    {
        if (jpeg_counter != 0)
        {
            fwrite(bytes, 512, 1, image);
        }
    }
    }

fclose(file);
return 0;

}
