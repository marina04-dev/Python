from random import seed
from random import randrange
from datetime import datetime

seed(datetime.now())

numbers = {}
for i in range(1,7):
    numbers[i]=0
    
print(numbers)

for _ in range(1000000):
    num = randrange(1,7)
    numbers[num] += 1
    
print(numbers)

for i in range(1,7):
    print(str(i) + ": " + str(numbers[i]/1000000))
