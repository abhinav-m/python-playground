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