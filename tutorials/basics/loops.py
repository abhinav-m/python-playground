# Basic syntax -> for item in iterable_object
# iterable-object-> list / strings /range  or some kind of collection
# item -> current value of iterator within the iterable object.

print("Number loop (list iterable)")
for number in [1, 2, 3]:
    print(number)

print("String iterable")
string = "abhinav"

for char in string:
    print(char)

print("Range iterable , includes start, excludes 10")
for x in range(1, 10):
    print(x)

# while loops run while the condition is 
x= 10
while x: # x is falsy when it is zero
    print(x)
    x = x - 1