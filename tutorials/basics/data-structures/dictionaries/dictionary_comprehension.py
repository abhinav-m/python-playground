# syntax {_:_ for _ in _}

numbers = dict(one=1,two= 2,three=3)

# Squaring each value for every key in dictionary using exponentiation operator **
squared_numbers = {key:value ** 2 for key,value in numbers.items()}
print(squared_numbers)

# Making a dictionary using a list.
cubed_numbers = {num:num**3 for num in [2,3,4,5,6]}
print(cubed_numbers)