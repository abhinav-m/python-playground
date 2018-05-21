# Collection of data without duplicate values and order.(unordered and unique)

# Creating a set
# using set constructor
my_set = set({1, 2, 3, 4, 5})
print(my_set)

# using normal dictionary initialisation without  key value pairs
your_set = {1, 2, 3, 4}

# checking if value is in set
print(5 in your_set)

# checking if value is in set
print(5 in my_set)
# items can't be accessed using index since there is no order.
# print(my_set[0]) throws error

varied_set = {"Abhinav", 123, 12.235}

# Looping through values in a set
for v in varied_set:
    print(v)

# Common set use - case : Removing duplicate data
duplicate_list = ["abhinav", "abhinav", "abcd"]


print(set(duplicate_list))
