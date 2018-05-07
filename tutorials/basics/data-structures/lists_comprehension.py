# Lists comprehension in python.
nums = [1, 2, 3, 4]
# Means for each value of x in nums, run the given function.
nums = [x*10 for x in nums]
print(nums)

numbers = [1, 2, 3, 4]
doubled_numbers = []
# Using a for loop the above code translates to:
for num in numbers:
    num = num * 2
    doubled_numbers.append(num)

print(doubled_numbers)

print([x/10 for x in nums])

# Upper casing the first letter in a list of names
names = ["abhinav", "akash", "paritosh"]

# Using in built method
print([name.capitalize() for name in names])

# Using string slicing.
print([name[0].upper() + name[1::] for name in names])

# Using with ranges.
print([num - 1 for num in range(1, 11)])


# Checking falsy values by wrapping in bool.
print([bool(val) for val in ["", {}, [], 0, -1, 1]])

# Conversion of values to string or any other type.
print([str(num) for num in [1.0, 2.5, 3.14, 9.62]])


# List comprehension with conditional logic.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if statement can be used with list comprehension
print([num for num in nums if num % 2 == 0])


# else statement can also be added.
# Note the difference in syntax here.
print([num * 2 if num % 2 == 0 else num/2 for num in nums])
