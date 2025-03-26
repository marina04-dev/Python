# First Numbers Input Check
# Lesson 6: Exercise 3

while (True):
    N = input("Enter an integer number bigger than 2 and 0 to exit: ").strip()
    if N.isdigit():
        number = int(N)
        if (number<2 and number!=0):
            print("The number must be bigger than the number 2!")
            continue
        elif (number==0):
            print("Exit")
            break
        else:
            for i in range(2,number):
                if number % i == 0:
                    print(f"Number {number} is not prime!")
                    break
                else:
                    print(f"Number {number} is prime!")
                    break
            
    else:
        print("Wrong Input! Enter only Numbers please!")
        continue
