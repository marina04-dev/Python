#execise_5 : digit-input-library
def is_odd(number):
    return number % 2 == 1
    
    
def is_even(number):
    return number % 2 == 0
    
    
def is_prime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number/2)):
        if number % i == 0:
            return False
    return True
        
def is_square(number):
    i = 0
    sq = 0
    while sq < number:
        i += 1
        sq = i*i
    return sq == number
def is_cube(number):
    i = 0
    q = 0
    while q < number:
        i += 1
        q = i*i*i
    return q == number
            
for i in range(1,101):
    print(f" {i}: ",end="")
    if is_odd(i):
        print("The number is odd",end=" ")
    if is_even(i):
        print("The number is even",end=" ")
    if is_prime(i):
        print("The number is prime",end=" ")
    if is_square(i):
        print("The number is square",end=" ")
    if is_cube(i):
        print("The number is cube",end=" ")
    print("")
    
