# Some common datatypes.

#bool -> true/false
test = True #Assigning true to test, notice capital T
test_2 = False #Uppercase F for false.

some_string ="A string"

test_array = [1,2,3,4] # List datatypes.

print(type(test_array))

print(type(some_string))
print(test)

# Python has dynamic data types.
# Variable accomodates all sorts of data according to type.
dynamic_var = 1
print(dynamic_var)

dynamic_var = True
print(dynamic_var)

dynamic_var = "test"
print(dynamic_var)

dynamic_var = None #Special type for None values
print(type(dynamic_var)) #Only one instance None of this class.

#None -> Pythons version of null. 
new_var = None
print(new_var)

str_one = "hello"
str_two = " world"

print(str_one + str_two)

#str_test = 8 + "test" this is not allowed in python. Strings cant be added to integers.
#print(str_test)

# conversion of data types.
decimal = 12.3242
decimal_toint = int(decimal)

# Notice it doesn't round, but 'chops' off the decimal part.
print(decimal_toint)
print(int(99.99))
print(str(22))