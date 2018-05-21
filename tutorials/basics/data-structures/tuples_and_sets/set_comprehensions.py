# Set comprehension

# Instead of specifying key value pairs, only value is provided here(unlike dictionaries.)
set_squared = {x**2 for x in range(10)}

# Note adding a colon converts it into a dictionary.
dict_squared = {x: x**2 for x in range(10)}
print(set_squared)
print(dict_squared)

# Creating a set out of a string(removing duplicates)
string_set = {ch for ch in "abhinav"}
print(string_set)  # order is not guaranteed.
