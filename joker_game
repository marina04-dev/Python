import random as rnd
user_numbers= set()
pick_numbers= set()
while(len(user_numbers)<5):
    num=int(input("Give me a number between 1 and 45: "))
    if (num>0 and num<=45):
        if num in user_numbers:
            print("Number already exists.Please give another number...")
        else:
            user_numbers.add(num)
    else:
        print("Number must be between 1 and 45.Please give another number...")
        continue
while (len(pick_numbers)<5):
    pick_numbers.add(rnd.randint(1,45))
if (user_numbers.isdisjoint(pick_numbers)):
    print("You found zero numbers")
else:
    total_numbers=len(user_numbers.intersection(pick_numbers))
    common_numbers=user_numbers.intersection(pick_numbers)
    if (total_numbers==5):
        print("Congrats!You won!!!")
    else:
        print(f"You found {total_numbers} number(s): {common_numbers} ")
