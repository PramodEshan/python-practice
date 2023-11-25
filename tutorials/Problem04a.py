# getting a word from user
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
word = input('Enter the word: ')

# check if it contains vowels
for char in vowels:  # get vowels one by one
    word = word.replace(char, 'g')  # check if it contains any vowels,if it is then replace it with g

# print changed word
print("Updated Word: ",word)
