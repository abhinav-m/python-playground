# A tuple is an ordered collection / grouping of items, it is immutable.

numbers = (1, 2, 3, 4)
print(numbers)

# Checking if value is in tuple
print(3 in numbers)

# Tuples are faster than lists, makes code safer, are valid keys in dictionaries.
# Example of a good usage of tuples

months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

print(months)

# Can be accessed using indexes just like lists.
print(months[0], months[-1])

# Creating office location dictionary with tuples as keys
# Note you can't use a list as a key.
locations = {
    (35.6895, 39.1597): "Tokyo office",
    (31.6895, -39.1597): "New york office",
    (42.6895, 11.1597): "San francisco office",

}

print(locations)

# Some dictionary methods return tuples
# Since keys are tuples themselves, returns nested tuples.
print(locations.items())

# iterating tuples
names = ("Abhinav", "Dhruv", "Pankaj")

for name in names:
    print(name)

tuple_example = ("A", "A", "B", "C", "D")

# count returns the number of times an element occurs in a tuple
print(tuple_example.count("A"))
print(tuple_example.count("B"))

# count returns the number of times an element occurs in a tuple
print(tuple_example.count("A"))
print(tuple_example.count("B"))

# returns the index of a tuple value
print(names.index("Dhruv"))

nested_tuple = (1, 2, 3, (4, 5), 6)
print(nested_tuple)

# tuples can be sliced using the same syntax shown earlier (for lists)
print(nested_tuple[0:])
print(nested_tuple[1:4:2])
