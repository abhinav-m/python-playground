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

# List comprehension with a range to calculate numbers divisible by 12
nums_div_by_12 = [num for num in range(1, 101) if num % 12 == 0]

# Removing the vowels from a string and getting a list
without_vowels_list = [char for char in "amazing" if char not in "aeiou"]

# Note how the join method works with both the generator and the iterable object.
without_vowels_string_1 = ''.join(
    [char for char in "amazing" if char not in "aeiou"])

without_vowels_string_2 = ''.join(
    char for char in "amazing" if char not in "aeiou")
