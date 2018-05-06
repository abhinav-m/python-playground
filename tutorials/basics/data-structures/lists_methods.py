# index method which returns index of given value
numbers = [1, 2, 3, 2, 5, 6]

print(numbers.index(2))
# prints the first 2 found (index 1)
# optional arguments -> start, stop

# starts looking for given argument from index 1.
print(numbers.index(2, 1))
# prints 1

# prints 3
print(numbers.index(2, 2))


names = ["Abhinav", "Athar", "Abhinav", "Abhinav", "Raju", "Athar", "Raju"]

# start is inclusive , end is not -> will throw error on 3,4
print(names.index("Raju", 3, 5))
