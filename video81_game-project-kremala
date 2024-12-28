# Game Project: Find the Letters of the Hidden Word 
from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())
guessed_letters = []


words = ["apple","orange","watermelon","melon","banana","kiwi","berries","strawberries","appricot","peach","cherry","golden-apple","pear","blueberries","gozzi-berries"]


hidden_word = words[randrange(len(words))]

# Repeat(while loop): step 2
# Ending with success: step 3
found = True
rounds = 10
for round in range(1,rounds+1):
    print(f"Round: {round}")
    #Check that the player put a string
    while True:
        letter = input("Give a letter: ").lower
        if len(letter)!=1:
            print("Error!Please give only ONE letter!")
        elif not letter.isalpha():
            print("Error!Please give only LETTERS!")
        elif letter in guessed_letters:
            print("You have already typed this letter!")
        else:
            break
    guessed_letters.append(letter)
    
    print(f"Letter {letter} exists {hidden_word.count(letter)} times in hidden word.")
    for char in hidden_word:
        if char in guessed_letters:
            print(char,end="")
        else:
            print("_",end="")
            found = False
    print("")
    
    if found:
        print(f"Congratulations! You found the hidden word which is: {hidden_word}")
        break
else:
    print("Failure! You ran out of rounds")
    print(f"The hidden word was: {hidden_word}")

