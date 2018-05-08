demo_list = ["a", "b", "c", "d"]

r = range(1, 10)
print(f"Length of list{len(list(r))}")

print(list(r))

# Lists starts at index 0 (same as arrays)
friends = ["Abhinav", "Dhruv", "Akshit"]
print(friends[0])

# Indexes can be accessed from backwards with a negative number( last index -> -1)
print(friends[-1])  # Prints Akshit (last index)

# in operator can be used with lists to check if the value exists in the list
print("Abhinav" in friends)  # prints true

print(s"abc" in friends)


colors = ["purple", "teal", "magenta", True, 22.3]

# Lists are iterable
for color in colors:
    print(color)

index = 0
numbers = [1, 2, 3, 4, 5]

while index < len(numbers):
    print(f"{index}:{numbers[index]}")
    index += 1

nums = [1, 2, 3, 4]
# Inserts object BEFORE index.
nums.insert(5, 4)
# With negative index , will insert BEFORE last index.
nums.insert(-1, 5)
print(nums)

# Empties a list
nums.clear()
print(f"After clearing, nums is {nums}")

# Removing from a selected index.
nums = [1, 2, 3, 4, 5]
# Removes from the end and returns removed element.
removed = nums.pop()
print(f"After popping 1, nums is {nums} ,removed value is {removed}")
# Removes from index 3(value 4)
removed = nums.pop(3)
print(
    f"After popping value from index 3, nums is {nums} ,removed value is {removed}")

first = nums.pop(0)
print(f"Removing first element, list is now {nums} removed is {first}")


# lists.remove method -> removes first occurrence of value found in string.
nums.remove(3)
print(f"Removes 3 from position 3 in list,list is now {nums}")

# Nested lists ( same as 2d arrays)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Printing value inside inner nested list
print(nested_list[0][-1])
