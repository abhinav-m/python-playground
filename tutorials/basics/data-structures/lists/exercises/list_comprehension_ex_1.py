# First letter of a list
first_letters = [name[0] for name in ["Ellie", "Tim", "Matt"]]

# Even numbers in a given list
even_numbers = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]

# Intersection of two lists
list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
intersection = [num for num in list_1 if num in list_2]

# Using string slice to reverse a word and lower() to lower it
words = ["Elie", "Tim", "Matt"]
reversed_and_lowered = [word[::-1].lower() for word in words]
