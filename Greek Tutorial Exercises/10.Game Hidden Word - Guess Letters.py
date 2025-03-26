# Game: Find The Letter In Hidden Word
# Lesson 10: Exercise 7
from random import randrange
from random import seed
from datetime import datetime

seed(datetime.now())

words = ["apple", "toast", "rose", "hat", "boy",
"love", "hope", "food", "sleep", "dog", "cat", "animals",
"children", "football", "window"]

hidden_word = words[randrange(len(words))]
print(hidden_word)

guessed_letters = []
max_rounds = 10
for rond in range(1, max_rounds+1):
    print(f"Round {rond}")
    while True:
        letter = input("Enter a letter: ").lower()
        if len(letter)!=1:
            print("Error! Enter Only One Letter Please!")
        elif not letter.isalpha():
            print("Error! Enter Only Letters Please!")
        elif letter in guessed_letters:
            print("Letter is Already Found!")
        else:
            break 
    guessed_letters.append(letter)
    print(f"Letter {letter} exists {hidden_word.count(letter)} in hidden word!")
    found = True
    for char in hidden_word:
        if char in guessed_letters:
            print(char, end="")
        else:
            print("_", end="")
            found = False
    print("")
    if found:
        print("Success! You found it!")
        break
    
else:
    print("Failure! Maximum Rounds Reached!")
    print("The hidden word was: " + hidden_word)
        
