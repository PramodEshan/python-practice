# getting a word from user
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
word = input('Enter the word: ')

# check if it contains vowels
for char in vowels:  # get vowels one by one
    if char.islower():  # check vowel is lowercase or not
        word = word.replace(char, 'g')  # for lowercase vowel replace it with g
    else:
        word = word.replace(char, 'G')  # uppercase, replace it with G

# print changed word
print("Updated Word: ", word)
