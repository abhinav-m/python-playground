some_list = [1, 2, 3, 4, 5, 6]

# Slice syntax  some_list[start:end:step]


# Slicing by providing first index only.
print(some_list[1:])

# Slicing from the last index using negative number
# prints last 3 numbers
print(some_list[-3:])

# Prints complete list.
print(some_list[:])

# By using 0 as the beginning index (start) or not providing start we can make a COPY of a list.
some_list_2 = some_list[0:]

# Since its a copy and doesn't reference the same in memory , this prints false.
print(some_list_2 is some_list)

# using end index. (exclusive) last index is not included (prints UPTO last index)
print(some_list[0:2])

# when using negative end indexes, counts from the end of the list.
# prints from the first index till BEFORE the last index.
print(some_list[1:-1])
print(some_list[1:-2])


# STEP example
# Printing odd numbers by taking 0th index and stepping 2. (from number 1)
print(some_list[::2])

# Printing even numbers by taking 0th index and stepping 2. (from number 2)

print(some_list[1::2])

# Negative step example
# When used with negative indexes, step parameter reverses the order of the list.

# Prints whole list reversed.
print(some_list[::-1])

# Prints list reversed with increased step value ( all values printed because no start and end indexes are provided.)
print(some_list[::-2])

print(some_list[:1:-1])

print(some_list[2::-1])

# Slice methods work the same on strings
# To reverse a string,
string = "My name is abhinav"
print(string[::-1])


# Modifying portions of a list
numbers = [1, 2, 3, 4, 5]

numbers[1:4] = ["a", "b"]
print(numbers)

# Slice can be chained in case of iterables such as strings.
names = ["abhinav", "athar", "raju"]
# prints reverse of "athar"
print(names[1][::-1])


# Swapping values in a list (swaps at index 1 and 2)
names[1], names[2] = names[2], names[1]
print(names)
