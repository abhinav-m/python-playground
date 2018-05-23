# using list comprehension.
def generate_evens():
    return [num for num in range(1, 50) if num % 2 == 0]

# using loop


# Mind the indentation while returning a value.( especially while looping to avoid returning a value earlier than intended.)
def generate_evens_loop():
    result = []
    for num in range(1, 50):
        if num % 2 == 0:
            result.append(num)
    return result


even_numbers = generate_evens()
even_numbers_loop = generate_evens_loop()
print(even_numbers)

print(even_numbers_loop)


def yell(what):
    return f"{what.upper()}!"


print(yell("ayy"))

# Define speak below:


def speak(animal="dog"):
    if(animal == "dog"):
        return "woof"
    elif(animal == "pig"):
        return "oink"
    elif(animal == "duck"):
        return "quack"
    elif(animal == "cat"):
        return "meow"
    elif(animal == "banana"):
        return "?"


print(speak())
print(speak("cat"))
print(speak("banana"))


def speak_dict(animal='dog'):
    noises = {'pig': 'oink', 'duck': 'quack', 'cat': 'meow', 'dog': 'woof'}
    return noises.get(animal, '?')


def speak_dict_2(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"
