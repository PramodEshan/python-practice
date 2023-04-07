# part i
# pre defined lists
Subjects = ["Maths", "Chem", "Physics", "English"]
Marks = [70, 65, 80, 75]


# define function to create dictionary
def convert(key, value):
    dict = {}
    for i in range(0, len(value)):
        dict[key[i]] = value[i]
    return dict


# print the dictionary
print(convert(Subjects, Marks))
