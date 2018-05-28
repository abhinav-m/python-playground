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

print(frequency([1,2,3,4,4,4],4))
print(frequency([True,False,True,True,False],False))
    