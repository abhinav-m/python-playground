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
    if(random() > 0.5):
        return "Heads"
    else:
        return "Tails"


print(coin_flip())

# default parameters in functions


def exponentiate(num, power=2):
    return num ** power


cubed = exponentiate(3, 3)

# Using with default parameter
squared = exponentiate(2)

print(cubed, squared)


def show_info(first_name="abhinav", last_name="mishra"):
    print(first_name, last_name)


# Note if we specify the parameter explicitly we don't need to stick to order.
show_info(last_name="test", first_name="abc")

show_info("Dhruv", "Dogra")

# functions can be passed as arguments, and also as default parameters.


def add(a, b):
    print(a+b)


def subtract(a, b):
    print(a-b)

# Adding a default parameter (a function , as an argument)

# ensure that default parameters are at the end since parameters are assigned in order.


def math(a, b, fn=add):
    fn(a, b)


# will add two numbers by default
math(1, 2)

# will subtract two numbers by default

math(5, 3, subtract)

# Keyword arguments:


def full_name(first_name, last_name):
    print(f"Your full name is {first_name} {last_name}")


full_name("Abhinav", "Mishra")

# Using keyword arguments (parameters are specified in function call)
# Only works in the case we know the parameters, and order of parameters doesn't matter anymore
# Note even though '=' operator is used in function call, this specifies it to be a keyword argument, and is not the normal assignment.
full_name(first_name="Mishra", last_name="Abhinav")


# Unpacking a dictionary
def display_names(first,second):
    print(f"{first} says hello to {second}")

names = {"first":"Colt","second":"Steele"}

# works fine
display_names("abhinav","mishra")

# can work with named parameters as well:
display_names(second="mishra",first="abhinav")

# To do the same with dictionary unpacking:
display_names(**names)


## Unpacking a dictionary with more examples:

def add_and_mult_nums(a,b,c,**kwargs):
    print(a+b*c)
    print("OTHER STUFF:")
    print(kwargs)
# note how the other things in the dictionary get's unpacked by **kwargs in the function definition
data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_mult_nums(**data,animal="cat")