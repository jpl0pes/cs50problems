import cs50

##Asking for the card number
while True:
    number = input("Number:")
    if number.isnumeric() == True:
        break;

##Get array of numbers of the credit card
card_numbers = str(number)

##Get every other number and multiply them by 2 and then sum their digits
array_x = list()
for i in range(len(card_numbers)-2,-1,-2):
    x = str(int(card_numbers[i])*2)
    for j in range(0,len(x),1):
        array_x.append(x[j])
    ##print(array_x)

sum_x = [int(i) for i in array_x]
##print(sum(sum_x))

sum_y = 0
for i in range(len(card_numbers)-1,-1,-2):
    sum_y = sum_y + int(card_numbers[i])
    ##print(sum_y)

##Add the first sum to the sum of all the numbers we didn't sum
##If number % 10 is not 0 then it's false
is_credit_card = False
if ((sum_y + sum(sum_x)) % 10 == 0):
    ##print("True")
    is_credit_card = True
else:
    ##print("False")
    is_credit_card = False


if is_credit_card == True:
    if card_numbers[0] == "3" and card_numbers[1] in ['4','7']:
        print("AMEX\n")
    elif card_numbers[0]=="5" and card_numbers[1] in ['1','2','3','4','5']:
        print("MASTERCARD\n")
    else:
        print("VISA")
else:
    print("INVALID\n")





