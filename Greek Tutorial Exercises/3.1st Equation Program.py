# 1st Equation Program: ax+b=0
# This program is a representing of 1st grade equation
# Equation: ax+b=0 if a==0 there is no solution
# In any other case the solution comes from the result of x=-b/a 
# Exercise 11 (If)
a = input("Enter a: ").strip()
b = input("Enter b: ").strip()
if a.isdigit() and b.isdigit():
    a = float(a)
    b = float(b)
    if a != 0:
        x = (-b)/a
        print(str(x) + " is the solution")
    else:
        print("It does not have a solution")
else:
    print("Wrong input!Please enter only digits!")
    
