# exercise 12 : Isosceles triangle (for-nested loops)
cross = True
while cross:
    num = input("Enter a number: ").strip()
    if num.isdigit():
        number = int(num)
        for i in range(0,number):
            for j in range(0,number-i-1):
                print(" ",end="")
            for j in range(0,2*i+1):
                print("*",end="")
            print("")
    else:
        cross = False
