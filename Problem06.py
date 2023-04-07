# Tuple created
example = ("40", "30", "10", "40", "80", "20", "70", "50", "40")
print("Original Tuple: ", example)
# tuple converted to a list
new = list(example)

# reverse the list
for i in range(0, int(len(new)/2)):
    x = new[i]
    new[i] = new[len(new)-1-i]
    new[len(new)-1-i] = x

example = tuple(new)    # convert new list to tuple and update tuple
print("Reversed Tuple: ", example)

print("index of element ‘70’: ", example.index("70"))  # output index of 70

new[new.index("10")] = 100  # replace 10 value by 100
example = tuple(new)    # convert new list to tuple and update tuple
print("Updated the value 10 as 100: ", example)

print("Number of occurrences of 40: ", example.count("40"))  # count number of occurrences of item 40
