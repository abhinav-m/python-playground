player_1 = input("Enter rock / paper / scissors ,player 1")

print("** __NO CHEATING__ **")
print("** __NO CHEATING__ **")
print("** __NO CHEATING__ **")
print("** __NO CHEATING__ **")
print("** __NO CHEATING__ **")
print("** __NO CHEATING__ **")
print("** __NO CHEATING__ **")
print("** __NO CHEATING__ **")

player_2 = input("Enter rock / paper scissors, player 2")

winner = None

if player_1 == player_2:
    print("Try again!")
elif player_1 == 'rock' and player_2 == 'scissors' or player_1 == 'scissors' and player_2 == 'rock':
    if player_1 == 'rock':
        winner = "player_1"
    else:
        winner = "player_2"
elif player_1 == 'paper' and player_2 == 'rock' or player_1 == 'rock' and player_2 == 'paper':
    if player_1 == 'paper':
        winner = "player_1"
    else:
        winner = "player_2"
elif player_1 == 'scissors' and player_2 == 'paper' or player_1 == 'scissors' and player_2 == 'rock':
    if player_1 == 'scissors':
        winner = 'player_1'
    else:
        winner = "player_2"

if winner:
    print(f'{winner} wins')
else:
    print("Noone won!")
