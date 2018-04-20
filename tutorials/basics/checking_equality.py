# To check equality, == operator can be used.
x = 13
y = 13

print(x == y)

# To check reference of variable in memory, is operator can be used.

a = [1, 2, 3]
b = [1, 2, 3]

# Will print false as both lists have different references.
print(a is b)

clone = a

# prints true
print(a is clone)

age = input("How old are you")

""" # 18-21 wristband
if age:
    age = int(age)
    if (age >= 18 and age < 21):
        print("wristband")
    # 21+ drink, normal entry
    elif(age >= 21):
        print("Normal entry")
    else:
        print("You're too young, sorry")
else:
    print("Please enter age") """


if age:
    age = int(age)
    if age >= 21:
        print("You can enter and drink")
    elif age >= 18:
        print("You can enter, need a wristband")
    else:
        # Every case is now <= 21
        print("You cant  come in, little one")
else:
    print("Invalid age")
