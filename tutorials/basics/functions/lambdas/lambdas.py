# Lambda functions are similar to anonymous functions in other languages. (eg Javascript)
def square(num): return num*num

# Syntax for lambda functions, returns square of number
# Automatically returns the expression after colon.
square2 = lambda num: num * num
print(square2(9))

# Lambda functions are used when passing functions as values to other functions.(generally)
# Write a lambda that accepts a single number and cubes it. Save it in a variable called cube.

cube = lambda num: num * num * num

##  Lambda function cubed.
cubed = lambda number: number ** 3

# Usage of lambda functions in higher order function such as map
def double(x) : return x*2

double(3)

test_list = [1,2,3,4,5]
doubles = list(map(lambda x:x*2,test_list))

print(doubles)