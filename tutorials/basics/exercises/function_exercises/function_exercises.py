'''
return_day(1) # "Sunday"
return_day(2) # "Monday"
return_day(3) # "Tuesday"
return_day(4) # "Wednesday"
return_day(5) # "Thursday"
return_day(6) # "Friday"
return_day(7) # "Saturday"
return_day(41) # None
'''


def return_day(num_of_day):
    days_dict = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday",
                 5: "Thurdsay", 6: "Friday", 7: "Saturday"}
    if num_of_day in days_dict:
        return days_dict[num_of_day]
    else:
        return None


def return_day_list(num):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num-1]
    except IndexError as e:
        return None


print(return_day(1))
print(return_day(2))
print(return_day(-1))
print(return_day(12))

print(return_day_list(1))
print(return_day_list(-7))


# Return last value in a list

def last_value(l):
    if(len(l) > 0):
        return(l[len(l) - 1])
    else:
        return None


print(last_value([1, 2, 3, 4, 5]))
print(last_value([]))

# Better way is to compare it by falsy value


def last_value_better(l):
    if l:
        return l[-1]
    else:
        return None


print(last_value_better([1, 2, 3, 4, 5]))
print(last_value_better([]))


def number_compare(num_1, num_2):
    if num_1 > num_2:
        return "First is greater"
    elif num_1 < num_2:
        return "Second is greater"
    else:
        return "Numbers are equal"


print(number_compare(1, 2))
print(number_compare(2, 1))
print(number_compare(1, 1))


def single_letter_count(str_1, ch):
    count = 0
    for char in str_1.lower():
        if char == ch.lower():
            count += 1
    return count


print(single_letter_count("abcdaaddc", "d"))

# Nested loop solution
def multi_letter_count(passed_str):
    multi_letter_dict = {}
    for char in passed_str:
        count = 0
        for cur_char in passed_str:
            if char == cur_char:
                count = count + 1
        multi_letter_dict[char] = count
    return multi_letter_dict

print(multi_letter_count("abcdaaddc"))


# Solution using dictionary comprehension:

def multiple_letter_count(passed_string):
    return {char:passed_string.count(char) for char in passed_string}

print(multiple_letter_count("awesome"))

def list_manipulation(l,method,position,value = None):
    if method == "remove":
        if position == "end":
            return l.pop()
        elif position == "beginning":
            return l.pop(0)
    elif method == "add":
        if position == "beginning":
             l.insert(0,value)
        elif position == "end":
             l.insert(len(l), value)
        return l
        
print(list_manipulation([2,3,4,5],"add","beginning",1))
print(list_manipulation([2,3,4,5],"add","end",6))


def is_palindrome(passed_str):
    start = 0 
    end = len(passed_str) - 1
    while(start <= end):
        if passed_str[start] != passed_str[end]:
            return False
        start += 1
        end -= 1
    return True 

print(is_palindrome("abca"))

print(is_palindrome("abba"))
# Using string slicing

def is_palindrome_sliced(passed_str):
    return passed_str == passed_str[::-1] # Reversing the order of the given string iterable

# Using slicing and white space correction
def is_palindrome_clean(passed_str):
    passed_str = passed_str.replace(" ","")
    return passed_str == passed_str[::-1] # Reversing the order of the given string iterable

print(is_palindrome_sliced("abba"))
print(is_palindrome_sliced("abca"))

print(is_palindrome_clean("abba"))
print(is_palindrome_clean("abca"))

def frequency(passed_list,search_term):
    count = 0
    for value in passed_list:
        if value == search_term:
            count+= 1
    return count

def frequency_count(passed_iterable, search_term):
    return passed_iterable.count(search_term)

print(frequency([1,2,3,4,4,4],4))
print(frequency([True,False,True,True,False],False))

def multiply_even_numbers(l):
    product = 1
    for num in l:
        if num % 2 == 0:
            product = product * num
    return product

print(multiply_even_numbers([2,3,4,5,6]))

def capitalize(passed_str):
    return(passed_str[:1].upper() + passed_str[1:])
capitalize("hello")

def compact(passed_list):
    return [item  for item in passed_list if item]

print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"]

def intersection(list_1,list_2):
   set_1 =   set(list_1)
   set_2 = set(list_2)
   return list(set_1.intersection(set_2))

print(intersection(['a','b','z'],['x','y','z']))

# solution using list comprehension
def intersection_2(l1,l2):
    return [ val for val in l1 if val in l2]

# solution by using sets and finding their intersection
def intersection_3(l1,l2):
    return[val for val in set(l1) & set(l2)] 

print(intersection_2(['a','b','z'],['x','y','z']))
print(intersection_3(['a','b','z'],['x','y','z']))


def isOdd(num):
    return num % 2 != 0

def partition(l,cb):
    return[[val for val in l if cb(val)] , [val for val in l if not cb(val)]]

print(partition([1,2,3,4,5],isOdd))


def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word


# argument unpacking:
def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

# wont work
#sum_all_values([1,2,3,4,5,6]) # throws error

# To unpack a collection we can use the keyword * while passing values as parameters to function.

collection = [1,2,3,4,5,6]
sum_all_values(*collection) # unpacks collection in the form of a tuple.

# Unpacking exercise:
# NO TOUCHING! =================================================================
def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
# NO TOUCHING! =================================================================

# Write your code below:

result1 = count_sevens(1,4,7)

# Unpacking the list and passing it as a tuple
result2 = count_sevens(*nums)

def calculate(**kwargs):
    # Switch operation alternate in python.
    operation_lookup = {
        'add':kwargs.get('first',0) + kwargs.get('second',0),
        'subtract':kwargs.get('first',0) - kwargs.get('second',0),
        'divide':kwargs.get('first',0) / kwargs.get('second',0),
        'subtract':kwargs.get('first',0) * kwargs.get('second',0),
    }
    # Check if float is present in kwargs, second parameter is default value.
    is_float = kwargs.get('make_float',False)
    # Check operation value
    operation_value = operation_lookup[kwargs.get('operation','')]
    # Assign result on the basis of keyword args check.
    if is_float:
        result = f"{kwargs.get('message','The result is')} ,{float(operation_value)}"
    else:
        result = f"{kwargs.get('message','The result is')} , {int(operation_value)}"
    return result

calc_dict = {"first":1,"second":2,"make_float":True,"operation":'add',"message":"The final value is"}

# To check 
print(calculate(**calc_dict))
        
