import random  # import random to use random module in code

# this support user inputs like 1,2,3 or 1,,2,,3 or 1,2,3, or ,1,2,3 or any type of comma pattern

numbers = input("Enter the numbers with comma separated: ")  # get comma separated numbers from user
numbers = numbers.split(",")    # separate entered numbers by comma
numbers = list(dict.fromkeys(numbers))  # remove duplicated NULL elements
numbers.remove("")  # remove NULL elements
number = [eval(i) for i in numbers] # convert all values to an integer value
total = 0   # to calculate sum
sqr = []    # to store square root of each number
odd = []    # to store odd numbers
even = []   # to store even numbers

maximum = max(number)   # get maximum numbers from number list

ranNum = random.choice(number)  # get random number from number list

for i in range(0, len(number)):     # cont index from 0 to length of number list
    total += number[i]  # calculate sum
    sqr.insert(i, pow(number[i], 2))    # calculate square root and store it in sqr list
    if number[i] % 2 == 0:  # check is number is divided by 2 or not
        even.append(number[i])  # if it is then number is even
    else:
        odd.append(number[i])   # if is not then number is odd

print("Sum of all elements: ", total)
print("Square each element: ", sqr)
print("Maximum number:  ", maximum)
print("Choose random number:    ", ranNum)
print("even numbers:    ", even)
print("odd numbers: ", odd)
