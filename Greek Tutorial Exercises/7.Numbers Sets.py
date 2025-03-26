# Numbers Sets (Lesson 7: Exercise 3)

N = 100
# Odd numbers in range 0-100
odd_set = set()
for i in range(1,N,2):
    odd_set.add(i)
print("\nOdd Numbers Set:")
print(odd_set)

# Even numbers in range 0-100
even_set = set()
for i in range(0,N+1,2):
    even_set.add(i)
print("\nEven Numbers Set:")
print(even_set)    

# Numbers multiplied 3 in range 0-100
cube_set = set()
for i in range(0,N,3):
    cube_set.add(i)
print("\nNumbers Multiplied By Three Set:")
print(cube_set)

# Primes numbers in range 0-100
primes_set = set()
for i in range(2,N+1):
    for j in range(2,i):
        if i % j == 0:
            break 
        else:
            primes_set.add(i)
print("\nPrime Numbers Set:")
print(primes_set)

set1 = even_set | cube_set
print("\nEven Numbers Or Multiplied By 3 Set:")
print(set1)

set2 = odd_set & primes_set
print("\nOdd Numbers And Prime Numbers Set:")
print(set2)

set3 = primes_set - odd_set
print("\nPrime Numbers That Are Not Odd Numbers Set:")
print(set1)

set4 = primes_set ^ odd_set
print("\nOdd Numbers Or Prime Numbers (Not Both Conditions At The Same Time) Set:")
print(set4)
