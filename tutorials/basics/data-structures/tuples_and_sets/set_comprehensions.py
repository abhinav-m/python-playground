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

# Set comprehension with conditionals

# Pulling vowels in a string

string_vowel_pull = {ch for ch in "testabc" if ch in "aeiou"}
print(string_vowel_pull)

# Check if all vowels are present in set
print(len(string_vowel_pull) == 5)
