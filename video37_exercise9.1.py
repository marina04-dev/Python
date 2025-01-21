hidden = 2
guess = 0
while True:
    guess = int(input("Try to guess the number I have hidden: "))
    if guess==hidden:
        print("You found it")
        break
    elif guess<hidden:
        print("Nope.It is smaller than the hidden.")
    else:
        print("The number is too big.")
        
