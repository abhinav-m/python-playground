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
