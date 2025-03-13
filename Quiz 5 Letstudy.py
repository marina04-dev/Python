##### Python Letstudy Quiz Unit 5 ######

# Question 1
def average(*args):
    total=length=0
    for i in args:
        total += i
        length += 1
    return total/length


# Question 2
def authenticate(username, password, role="Student"):
    if (username == "Demo" and password == "Demo"):
        return role == False if role == "Student" else True
    else:
        return False

print(authenticate(username="Demo",password="Demo"))
print(authenticate(username="Demo",password="Demo",role="Admin"))


# Question 3
def demofunc(*, char='*', rows=2, columns=4):
    for i in range(rows):
        for j in range(columns):
            print(char, end='')
        print()

demofunc()
demofunc(rows=5, columns=8)
demofunc(rows=5, columns=8, char="$")



# Question 4
def demofunc2(*args, **kwargs):
    mylist = [i**2 for i in args if i%2==0]
    mydict = {x:y for x,y in kwargs.items() if y%2==0}
    if args:
        mydict['args'] = sum(mylist)
    return mydict

print(demofunc2())
print(demofunc2(2,4,5))
print(demofunc2(first=4, second=5))
print(demofunc2(3, 1, 2, 4, 5, first=2, second=5, value=4))
print(demofunc2(5, value=2))



# Question 9
import random

def random_numbers(*,from_n=1, upto_n=100, total_n=5):
    for num in range(total_n):
        yield random.randint(from_n,upto_n)

for number in random_numbers():
    print(number)


# Question 10
def lendata(data):
    return data.upper()

def lenlower(data):
    return len(data) == 3


values = ['George','Joe','Bob','Pam','Mary']
valuesUpper = list(map(lendata, values))
valuesLower = list(filter(lenlower,valuesUpper))
print(values)
