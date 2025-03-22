x = int(input("Give me a number: "))
y = int(input("Give me a number: "))
z = int(input("Give me number: "))
if (x>y and x>z and x!=y and x!=z):
    print("The greatest number is x")
elif (y>x and y>z and y!=x and y!=z):
    print("The greatest number is y")
else :
    print("The greatest number is z")
    
