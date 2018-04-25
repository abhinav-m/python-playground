import random

random_number = random.randint(1, 10)


play = True

while play:
    print("Guess the number")
    number = int(input())
    if number < random_number:
        print("Too low")
    elif number > random_number:
        print("Too high")
    else:
        print("You guessed correct")
        play = input("Do you want to play again?")
        if play == 'y' or play == 'Y':
            play = True
        else:
            play = False
