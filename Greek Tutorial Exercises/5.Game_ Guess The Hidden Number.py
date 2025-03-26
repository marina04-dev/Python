# Guess The Hidden Number: Game
# Exercise 9.1, 9.2, 9.3 (while-break-continue)
from random import randrange
from datetime import datetime
from random import seed

num = randrange(0,50)
tries = 0
while tries < 5:
    number = input("Guess and enter a number: ").strip()
    if number.isdigit():
        numbers = int(number)
        if numbers == num:
            print("Yoou woon!!")
            break
        elif numbers > num:
            print("Too big!!!")
            tries += 1
        else:
            print("Too low!!!")
            tries += 1
