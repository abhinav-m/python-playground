
# Strings can be concatenated using the plus oeprator'+'
a = "Check "
b = " b_Check"
c = a + b
print(c)

# f strings can be used to interpolate variables in strings. New in python -> 3.6+
# implicitly converts variables to strings.
d = f"{a} two {b}"
print(d)

# Older way -> 2.x -> 3.5 format
d = "{} test {}".format(a, b)  # Must be inserted in order.
print(d)

# Accessing characters
test = "abc"

print(test[0])
print(test[1])

# Negative indexes can be accessed to get values of character from back.
print(test[-1])
