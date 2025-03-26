# LOTTO Lucky sixies Machine (Lesson 7: Exercise 2)
from random import seed 
from random import randrange
from datetime import datetime

seed(datetime.now())

i = 0
columns = []
while True:
    column = set()
    # 2 numbers in range 10-19
    rand_number = randrange(10,20)
    column.add(rand_number)
    while True:
        rand_number = randrange(10,20)
        if rand_number not in column:
            column.add(rand_number)
            break 
        
    # 2 numbers in range 20-39
    rand_number = randrange(20,40)
    column.add(rand_number)
    while True:
        rand_number = randrange(20,40)
        if rand_number not in column:
            column.add(rand_number)
            break 
        
    # 1 even number in range 1-9 
    rand_number = 2 * randrange(1,5)
    column.add(rand_number)
    
    # 1 odd number in range 41-49 
    rand_number = randrange(41,50,2)
    column.add(rand_number)
    
    if column not in columns:
        columns.append(column)
        i += 1 
        if i==10:
            break 
        
for column in columns:
    print(column)
