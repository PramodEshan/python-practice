# problem 02
# part a
while True:
    number1 = int(input('Enter first number: '))  # getting first number from user
    number2 = int(input('Enter second number: '))  # getting second number from user

    # get which operation user want to perform
    operation = int(
        input('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division \nSelect operations you want to do: '))

    # compute user selected operation
    match operation:
        case 1:
            print(number1, '+', number2, '=', number1 + number2)  # output addition
        case 2:
            print(number1, '-', number2, '=', number1 - number2)  # output subtraction
        case 3:
            print(number1, '*', number2, '=', number1 * number2)  # output Multiplication
        case 4:
            print(number1, '/', number2, '=', number1 / number2)  # output Division
        case _:
            print('operation selecting error')

    output = input('Need to calculate another number? (Y/N) ')
    if (output == 'N') + (output == 'n'):
        break
