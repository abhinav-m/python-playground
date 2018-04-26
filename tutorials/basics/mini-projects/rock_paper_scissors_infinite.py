
import random

keepPlaying = True
while keepPlaying:
    ai_move = random.choice(["rock", "paper", "scissors"])
    player_move = input("rock , paper or scissors")
    print(f"AI chose {ai_move}")
    if player_move == ai_move:
        print("Tie!")
    elif ai_move == 'rock' and player_move == 'scissors':
        print("Ai wins :(")
    elif ai_move == 'scissors' and player_move == 'paper':
        print("Ai wins :(")
    elif ai_move == 'paper' and player_move == 'rock':
        print("Ai wins :(")
    else:
        print("You win! :D")
    choice = input("Do you want to keep playing? (y/n)")
    if(choice == "y" or choice == "Y"):
        keepPlaying = True
    else:
        keepPlaying = False
