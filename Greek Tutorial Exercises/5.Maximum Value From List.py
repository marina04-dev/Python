# Maximum value from list with 10 random numbers
# This program initializes a list with 10 unique nums in range 0 and 30
# And Finds the Maximum Value
# Exercise 4 (while)
from random import randrange
from datetime import datetime
from random import seed

my_list = []
while len(my_list)<10:
    num = randrange(0,20)
    if num not in my_list:
        my_list.append(num) 
    else:
        continue
print(my_list)

i = 1
maximum = my_list[0]
for i in range(len(my_list)):
    if my_list[i] > maximum:
        maximum = my_list[i]
    else:
        continue
print(maximum)
    
