# define dict1 and dict2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

# create dict3 and add dict1 and dict2
dict3 = {**dict1, **dict2}
print(dict3)

# or simply we can update one dictionary
dict1.update(dict2)
print(dict1)