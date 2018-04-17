name = input()

if name == 'Jon Snow':
    print("You know nothing")
elif name == 'Arya Stark':
    print("Valar Morghulis")
else:
    print("Carry on")


# Truthy and falsy values in python

if 0:
    print("Falsy.")
# 1 is truthy
if 1:
    print("Truthy")


# Empty strings are falsy in python.

test = input()
if test:
    print("You said " + test)
else:
    print("SAY SOMETHING!!")

# Can be compared directly.
print("a" == "b")
