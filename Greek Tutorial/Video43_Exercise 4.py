primes_list = []
for N in range(2,101):
    for i in range(2,N):
        if N%i==0:
            break
    else:
        primes_list.append(N)
        
tuple_primes = tuple(primes_list)
print(tuple_primes)
