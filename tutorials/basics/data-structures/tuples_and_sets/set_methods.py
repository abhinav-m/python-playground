# add function
my_set = {1, 2, 3, 4, 5}
print(my_set)

# add a value, successfull
my_set.add(6)
print(my_set)

# add a value, unsuccessful, but doesn't throw error.
my_set.add(6)
print(f"Doesn't add 6 again, {my_set} ")

# remove function

# successful if element is in the set.
my_set.remove(3)
print(f"Removing 3, {my_set}")

# # throws error if not present in set.
# my_set.remove(3)

# If we don't want it to throw an error if it doesn't exist, discard method can be used.
my_set.discard(3)  # doesn't throw an error.

# successful removal.
my_set.discard(1)

#
copy_of_set = my_set.copy()


set_new = set([1, 2, 3, 4, 5])

set_new.clear()

# clears the set.
print(set_new)


# Mathematical set methods

math_students = {"Abhinav", "Manish", "Dhruv"}

science_students = {"Akash", "Abhinav", "Lekhraj", "Manish"}

# Getting union of a set.
print(math_students | science_students)

# Intersection of a set.
print(math_students & science_students)
