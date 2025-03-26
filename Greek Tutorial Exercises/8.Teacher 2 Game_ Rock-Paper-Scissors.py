# Game: Rock-Paper-Scissors - Edition Teacher(2)
from random import seed
from random import randrange
from datetime import datetime  

seed(datetime.now())  

round = 0
score = [0, 0] # Player, computer
history = []
while True:
    round += 1
    print("Round " + str(round))

    # User Input
    player_input_str = input("Choose: ")
    while player_input_str not in ["rock", "scissors", "paper"]:
        print("Wrong input. Choices: rock, scissors, paper")
        player_input_str = input("Choose: ")

    if player_input_str == "rock":
        player_input_int = 0
    elif player_input_str == "scissors":
        player_input_int = 1
    else:
        player_input_int = 2

    # Computer Choice
    computer_choice_int = randrange(3)
    if computer_choice_int == 0:
        computer_choice_str = "rock"
    elif computer_choice_int == 1:
        computer_choice_str = "scissors"
    else:
        computer_choice_str = "paper"

    diff = player_input_int - computer_choice_int

    if diff == -1 or diff == 2:
        winner = "player"
    elif diff == -2 or diff == 1:
        winner = "computer"
    else:
        winner = "no winner"

    # Score Check

    if winner == "player":
        score[0] += 1
    elif winner == "computer":
        score[1] += 1

    # enimerwsi tou istorikou
    history.append("Round " + str(round) + ": Player: " + player_input_str + ", Computer: " + computer_choice_str + ", Score: " + str(score[0]) + "-" + str(score[1]))

    print("Computer picks: " + computer_choice_str)
    print("Player-Computer: " + str(score[0]) + "-" + str(score[1]))

    if score[0] == 3:
        print("Player wins! ")
        print("")
        for history_item in history:
            print(history_item)
        break
    elif score[1] == 3:
        print("Computer wins! ")
        print("")
        for history_item in history:
            print(history_item)
        break

    print("====================\n")
