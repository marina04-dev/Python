from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

round = 0
score = [0, 0] #Player _ Computer
history =  []
while True:
    round += 1
    print("Round " + str(round))
    
    #Player input
    player_input = input("Choose: ")
    while player_input not in ["rock","scissors","paper"]:
        print("Wrong input.Choices: rock, scissors, paper")
        player_input = input("Choose: ")
    
    
    #Computer choice
    compputer_random = randrange(3)
    if computer_random == 0:
        computer_choice = "rock"
    elif computer_random == 1:
        computer_choice = "scissors"
    else:
        computer_choice = "paper"
        
    
    #Check who the winner is
    if player_input == "rock":
        if computer_choice == "rock":
            winner = "no winner"
        elif computer_choice == "paper":
            winner = "computer"
        else:
            winner = "player"
    elif player_input == "paper":
        if computer_choice == "rock":
            winner = "player"
        elif computer_choice == "paper":
            winner = "no winner"
        else:
            winner = "computer"
    else: #player_input == "scissors:
        if computer_choice == "rock":
            winner = "computer"
        elif computer_choice == "paper":
            winner = "player"
        else:
            winner = "no winner"
            
    #Score holding
    if winner == "player":
        score[0] += 1
    elif winner == "computer":
        score[1] += 1
    
    #History reload
    history.append("Round " + str(round) + ": Player: " + player_input + ", Compputer: " + computer_choice + ", Score: " + str(score[0] + "-" + str(score[1])))
    
    #Winner printing
    print("Computer picks: " + computer_choice)
    print("Player-Computer: " + str(score[0]) + "-" + str(score[1]))
    
    print("================================\n")
    
    
    
    #Ending case based in the score
    if score[0] == 3:
        print("Player won!")
        print("")
        for history_item in history:
            print(history_item)
        break
    elif score[1] == 3:
        print("Computer won!")
        for history_item in history:
            print(history_item)
        break
    
        
