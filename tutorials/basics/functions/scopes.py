# Any variable inside a function is only available in function
def hello_world():
    hello_str = "Hello world"
    print(hello_str)


hello_world()

#  Can't do this -> print(hello_str)

total = 0


def increment():
    global total  # Referring to global total
    # If the above statement was not written, python would throw an error (assigning variable without declaration)
    total += 1
    print(total)


increment()


# non local keyword
# Let's us modify a parents variable in  a nested function:

def outer():
    count = 0

    def inner():
        nonlocal count  # this variable is defined in  a nested scope
        count += 1
        return count
    return inner()


print(outer())

# Must be first line of the function to create a doc


def prints_hello_world():
    """This function prints hello world"""
    print("Hello world")


print(prints_hello_world())

# To print doc for a function
doc = prints_hello_world.__doc__

print(doc)
