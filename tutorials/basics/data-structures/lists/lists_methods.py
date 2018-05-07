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

# prints count of a value in a list.
cnt = names.count("Raju")
print(cnt)


# If value is not present, returns 0 , unlike index which throws error.
print(names.count("akash"))
# Logs 0

nums = [1, 2, 3, 4, 5]

# Reverses list in place
nums.reverse()

print(nums)


# sorts list in place
nums = [5, 2, 1, 3, 6]

nums.sort()

print(nums)


# join method -> string method which takes iterable argument
# and joins them using the given delimiter.

words = ["I", "am", "learning", "python"]
print("#".join(words))
