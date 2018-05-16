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
print(locations.items())
