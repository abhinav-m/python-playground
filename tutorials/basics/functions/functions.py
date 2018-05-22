from random import random
# Function definition syntax

# defining function


def hello_world():
    print("Hello world")


# invoking function
hello_world()


# Returning values from function
def square(num):
    return num**2


squared_num = square(2)

print(squared_num)


def coin_flip():
    r = random()
    if(r > 0.5):
        return "Heads"
    else:
        return "Tails"


print(coin_flip())
