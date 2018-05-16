# syntax {_:_ for _ in _}

numbers = dict(one=1, two=2, three=3)

# Squaring each value for every key in dictionary using exponentiation operator **
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)

# Making a dictionary using a list. (iterable collection)
cubed_numbers = {num: num**3 for num in [2, 3, 4, 5, 6]}
print(cubed_numbers)

# An example using strings and loops

str_1 = "abhinav"
str_2 = "mishraa"

# In this case the iterable object is the string, assigning key value pairs of both strings to each other.
interleaved = {str_1[i]: str_2[i] for i in range(0, len(str_1))}
print(interleaved)

# Uppercasing dictionary example
abhinav = {"name": "abhinav", "age": "25", "sex": "male"}

abhinav_caps = {k.upper(): v.upper() for k, v in abhinav.items()}
print(abhinav_caps)

# Generating even/odd numbers in a dictionary using conditional logic
even_odd = {num: ("even" if num % 2 == 0 else "odd") for num in range(1, 16)}

print(even_odd)

# Keys can also have conditional logic
abhinav_small_caps = {(k.lower() if k == 'NAME' else k): v.upper()
                      for k, v in abhinav_caps.items()}
print(abhinav_small_caps)
