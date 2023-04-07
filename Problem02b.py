# get three numbers from user
number1 = input('enter the number 01: ')
number2 = input('Enter the number 02: ')
number3 = input('Enter the number 03 ')
m = "Maximum number is: "

# find max
if number1 > number2:  # compair number 1 and number 2
    if number1 > number3:  # if number 1 is greater than number 2, check it also greater than number 3
        print(m, number1)  # if it is, then max number is number 1
    else:
        print(m, number3)  # if it is not then max number is number 3
elif number2 > number3:  # number 2 is greater. so check number 2 is greater than number 3
    print(m, number2)   # if it is number 2 is max number
else:
    print(m, number3)   # if it is not number 3 is max number
