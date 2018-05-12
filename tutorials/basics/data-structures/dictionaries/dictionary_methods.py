dict_abhinav = {
    "name": "Abhinav",
    "age": 25,
    "salary": 1000000
}

# To copy a dictionary
# Note only the values are copied, a new reference is created in memory.
dict_abhinav_copy = dict_abhinav.copy()

# To check references , thus a new reference is passed to dict_abhinav_copy.
print(dict_abhinav_copy is dict_abhinav)

print(dict_abhinav)

# To clear a dictionary:
print(dict_abhinav.clear())

print(dict_abhinav_copy)

# Creating a dictionary from keys.

# Assigns each value in the iterable object to the given value
print({}.fromkeys(["age"], "25"))
# Note that each value will be assigned to the value passed in the second parameter.
print({}.fromkeys([1, 2, 3, 4, 5], ["a", "b", "c", "d", "e"]))

# This can be useful while setting a default value.
new_user = dict.fromkeys(['name', 'email', 'score', 'profile_bio'], "unknown")

print(new_user)

# get method To  get the value of a key in a dictionary.

print(dict_abhinav_copy.get("name"))
# Note when the value is not present, it returns None. ( can be useful to perform checks of keys in dictionaries)
print(dict_abhinav_copy.get("sex"))
