# syntax {_:_ for _ in _}

numbers = dict(one=1,two= 2,three=3)

# Squaring each value for every key in dictionary using exponentiation operator **
squared_numbers = {key:value ** 2 for key,value in numbers.items()}
print(squared_numbers)

# Making a dictionary using a list. (iterable collection)
cubed_numbers = {num:num**3 for num in [2,3,4,5,6]}
print(cubed_numbers)

# An example using strings and loops

str_1 = "abhinav"
str_2 = "mishraa"

# In this case the iterable object is the string, assigning key value pairs of both strings to each other.
interleaved = {str_1[i]:str_2[i] for i in range(0,len(str_1))}
print(interleaved)