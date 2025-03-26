# Memory Game With Cards - Lesson 6: Exercise 7.1-7.4
from random import randrange
from datetime import datetime
from random import seed

my_list1 = []
n=0
while n<4:
    i = randrange(1,5)
    if i in my_list1:
        continue
    else:
        my_list1.append(i)
        n+=1
        
my_list2 = []
x=0
while x<4:
    i = randrange(1,5)
    if i in my_list2:
        continue
    else:
        my_list2.append(i)
        x+=1
    
my_list1.extend(my_list2)
N=len(my_list1)
state = []
for _ in range(0,N):
    state.append("closed")
    
active_game = True 
found = 0
score = 0
while active_game:
    score+=1 
    # read 1st position
    first_position = input("Enter the 1st position(0-(N-1) and closed): ")
    if first_position.isdigit():
        first_pos = int(first_position)
        while (first_pos < 0 or first_pos >= N) or state[first_pos] == "open":
            print("Out of table's bounds/Already opened card!")
            continue
    else:
        print("Enter only digits please!")
        continue
    
    # read 2nd position
    second_position = input("Enter the 2nd position(0-(N-1) and closed): ")
    if second_position.isdigit():
        second_pos = int(second_position)
        while (second_pos < 0 or second_pos >= N) or state[first_pos] == "open" or second_pos == first_pos:
            print("Out of table's bounds/Already opened card!")
            continue
    else:
        print("Enter only digits please!")
        continue
    
    # change state: both temp_open
    state[first_pos] = "temp_open"
    state[second_pos] = "temp_open"
    
    # Current state Printing
    print("")
    for position in range(N):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(my_list1[position], end="")
        else:
            print(my_list1[position], end="")
    print("")
    
    # check if same then open, else closed
    if my_list1[first_pos] == my_list1[second_pos]:
        state[first_pos] == "open"
        state[first_pos] == "open"
        print("Success!")
        found += 2 
    else:
        state[first_pos] = "closed"
        state[second_pos] = "closed"
        print("Failure!")
        
    # print current state 
    print("")
    for position in range(N):
        if state[position] == "closed":
            print("_", end="")
        elif state[position] == "open":
            print(my_list1[position], end="")
        else:
            print(my_list1[position], end="")
    print("")
    
    if found == N:
        print("Bravo!! Game finished! Score = " + str(score))
        active_game = False
            
