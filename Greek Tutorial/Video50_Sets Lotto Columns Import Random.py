from random import seed
from random import randrange
from datetime import datetime

i = 0
columns = []
while True:
    seed(datetime.now())
    
    column = set()
    
    # from 10 to 19
    
    rand_number = randrange(10,20)
    column.add(rand_number)
    
    while True:
        rand_number = randrange(10,20)
        if rand_number not in column:
            column.add(rand_number)
            break
    
    # from 20 to 39
    rand_number = randrange(20,40)
    column.add(rand_number)
    
    while True:
        rand_number = randrange(20,40)
        if rand_number not in column:
            column.add(rand_number)
            break
    
    # from 1 to 9 EVEN
    rand_number = 2 * randrange(1,5)
    column.add(rand_number)
    
    
    # from 40 to 49 ODD
    rand_number = randrange(41,49,2)
    column.add(rand_number)
    
    if column not in columns:
        columns.append(column)
        i += 1
        if i ==10:
            break
for column in columns:
    print(column)
