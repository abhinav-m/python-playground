# Dictionaries are a data structure consisting of key -value pairs (same as objects / maps in javascript or java)
cat = {"name": "blue", "age": 3.5, "isCute": True}

print(cat)

# Another way to create a dictionary

dictionary_2 = dict(name="Abhinav", age="25", works="b4s")

print(dictionary_2)

age_str = "age"

# Accessing dictionary values.
print(dictionary_2["name"])

print(dictionary_2["age"])

print(dictionary_2[age_str])

print("Values in dictionaries")

# Accessing all dictionary values
for value in cat.values():
    print(value)

print("Keys in dictionaries")
# Accessing all dicionary keys
for key in cat.keys():
    print(key)

# Accessing both inside loop
for k, v in cat.items():
    print(f"key is {k} value is{v} ")
