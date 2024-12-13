#artioi
odd_set = set()
for i in range(0,100,2):
    odd_set.add(i)
    
print(odd_set)
print(len(odd_set))


#perittoi 
perittoi_set = set()
for i in range(-1,100,2):
    perittoi_set.add(i)
    
print(perittoi_set)
print(len(perittoi_set))

#pollaplasia tou 3
od_set = set()
for a in range(0,100):
    if a%3==0:
        od_set.add(a)
    else:
        continue
    
print(od_set)
print(len(od_set))

#odd kai pollaplasia tou 3
odi_set = set()
for a in range(100):
    if a%2==0 and a%3==0:
        odi_set.add(a)
    else:
        continue
print(odi_set)
print(len(odi_set))

#prwtoi arithoi
N=100
primes_set = set()
for number in range(2,N+1):
    for v in range(2,number):
        if number%v==0:
            break
    else:
        primes_set.add(number)
print(primes_set)
print(len(primes_set))


#artioi h pollaplasia tou 3
set1 = odd_set | od_set
print(set1)


#perittoi prwtoi
set2 = perittoi_set & primes_set
print(set2)


set4 = primes_set ^ odd_set
print(set4)
