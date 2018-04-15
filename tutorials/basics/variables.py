#Variables
x = 100
y = "Hello"
z = "true"

new_line = "hi\nthere"
print(new_line)

print(x,y,z)

# Multiple assignments
a,b,c=1,2,"test"

print(a,b,c)

str_1 = "test"
str_2 = 'test'
str_3 = ' check "test"'

print(str_1,str_2,str_3)


#Variables must start with letters or underscore _ .
cat = "kityy"
_cat = "kitty"

#Variables are case sensitive
CAT = "test"
print(cat,_cat,CAT)

#variables must not start with numbers.
#1_test = 9;

#only _ is allowed in variable names.
hello_world = "Hello world"
print(hello_world)


#snake case is a general best practice
num_of_players = 3

print(num_of_players)

#constants are uppercased.
PI = "3.14"

#classes are usually UpperCamelCased

# double underscore variables (starting and ending with __) are used to signify variables 
# that must not be changed / messed with (might encounter in open-source/big projects)
__system_helper__  = "SIGINT" 
 