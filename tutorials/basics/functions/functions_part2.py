# *args -> Special parameter passed to a function (like rest parameter in js) , gathers REMAINING arguments passed to function as a tuple.
# can be called whatever, must start with *

def sum_all_nums(*args):
    sum = 0
    for num in args: # Note that the values are stored in the form of a tuple.
        sum += num
    print(sum)

sum_all_nums(4,5,6,7)

def concat_all_strings(*strings):
    concatted = ""
    for string in strings:
        concatted += string 
    return concatted

print(concat_all_strings("a","b","c"))

def contains_purple(*args):
    if "purple" in args:
        return True
    return False

print(contains_purple("purple","orange",1,2,3,"green")) 

print(contains_purple("red","blue","yellow"))

#**kwargs -> Special parameter passed to a function, gathers value passed to a function in the form of a dictionary.
#must start with **



# Using keyword arguments (parameters are specified in function call)
# Only works in the case we know the parameters, and order of parameters doesn't matter anymore
# Note even though '=' operator is used in function call, this specifies it to be a keyword argument, and is not the normal assignment.

# def favorite_colors(**kwargs):
#     for person,color in kwargs.items(): #Instead of tuples ** gathers the value in the form a dictionary.
#         print(f"{person}s favourite color is {color}")

# favorite_colors(abhinav="red",dhruv="blue")

# Note , *args **kwargs both capture only the REMAINING values passed to the function if more values are mapped in the functions
#earlier, they will be treated like so:

def favorite_colors(dhruv,**kwargs):
    for person,color in kwargs.items(): #Instead of tuples ** gathers the value in the form a dictionary.
        print(f"{person}s favourite color is {color}")
        print(dhruv)

# Since we are passing parameterised (keyword arguments to the functions) order doesn't matter, note how "dhruv" is still
# assigned it's value, and abhinav is assigned to rest.
favorite_colors(abhinav="red",dhruv="blue")