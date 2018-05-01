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

print("abc" in friends)


colors = ["purple", "teal", "magenta", True, 22.3]

# Lists are iterable
for color in colors:
    print(color)

index = 0
numbers = [1, 2, 3, 4, 5]

while index < len(numbers):
    print(f"{index}:{colors:[index]}")
    index += 1
