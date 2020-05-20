import cs50

while True:
    string = input("Height:")
    if string.isnumeric() == True:
        height = int(string)
        if height > 0 and height < 9:
            break;

for i in range(1,height+1,1):
        print(" " * (height-i) + "#" * (i) + "  " + "#" * (i), end='\n' )