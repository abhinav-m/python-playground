user_info = {"name": "Abhinav", "age": "25", "sex": "Male"}

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
# Use a loop to add together all the donations and store the resulting number in a variable called total_donations
for v in donations.values():
    total_donations += v

# This code picks a random food item:
from random import choice  # DON'T CHANGE!
food = choice(["cheese pizza", "quiche", "morning bun",
               "gummy bear", "tea cake"])  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")

# Another solution using get:

quantity = bakery_stock.get(food)

if quantity:
    print(f"{quantity} left")
else:
    print("We don't make that")


# DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
                   "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notications", "achievements"]

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0.  Save the result to a variabled called initial_game_state
initial_game_state = dict.fromkeys(game_properties, 0)
# Another solution initial_game_state = {}.fromkeys(game_properties,0)

inventory = {'croissant': 19, 'bagel': 4,
             'muffin': 8, 'cake': 1}  # DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"

stock_list.update({"cookie": 18})

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0, len(list1))}
print(answer)

# Key value pairs
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# Directly creating a dictionary with the person nested list
answer_2 = dict(person)
print(answer_2)

# Iterating over the dictionary
answer_3 = {k: v for k, v in person}

answer_4 = {item[0]: item[1] for item in person}

print(answer_3, answer_4)
