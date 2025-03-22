hidden = 2
guess = 0
max_tries = 5
tries = 0
while tries<=5:
    guess = int(input("Try to guess the number I have hidden: "))
    if guess==hidden:
        print("You found it")
        break
    elif guess<hidden:
        print("Nope.It is smaller than the hidden.")
        tries += 1
        if tries == 5:
            print("You ran out of tries.Maybe next time.")
            break
    else:
        print("The number is too big.")
        tries += 1
        if tries == 5:
            print("You ran out of tries.Maybe next time.")
            break
        
