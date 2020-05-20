#include "helpers.h"
#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            int average = round((float)(image[i][j].rgbtBlue+image[i][j].rgbtGreen+image[i][j].rgbtRed)/3);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }

    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            //Formula for getting into the Sepia's values
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);


            //Controll for limit of 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int halfWidth = round((float)1/2 * width);
        for (int j = 0; j < halfWidth ; j++)
        {
           RGBTRIPLE tmp = image[i][j];
           image[i][j] = image[i][width-j-1];
           image[i][width-j-1] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width ; j++)
        {
            //Totals and Total pixels around
            int total_red = 0;
            int total_green = 0;
            int total_blue = 0;
            int total_pixels = 0;

            for (int n = -1; n < 2; n++)
            {
                if (i + n >= 0 && i + n < height)
                {
                  for (int m = -1; m < 2; m++)
                  {
                     if (j + m >= 0 && j + m < width)
                     {
                      total_red = image[i+n][j+m].rgbtRed + total_red;
                      total_green = image[i+n][j+m].rgbtGreen + total_green;
                      total_blue = image[i+n][j+m].rgbtBlue + total_blue;
                      total_pixels++;
                     }
                  }
                }
            }

            image[i][j].rgbtRed = round((float)total_red/(float)total_pixels);
            image[i][j].rgbtGreen = round((float)total_green/(float)total_pixels);
            image[i][j].rgbtBlue = round((float)total_blue/(float)total_pixels);
        }

    }
    return;
}
