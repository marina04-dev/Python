# First Numbers Tuple
# Lesson 6: Exercise 4

primes_list = []
for i in range(2,101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes_list.append(i)
            
primes = tuple(primes_list)
print(primes)
