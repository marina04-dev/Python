# Square numbers (while loop with input check)
# Exercise 1 (While)
while True:
    num = input("Enter a number or quit to exit: ").strip().lower()
    if num.isdigit():
        nums = int(num)
        print(num**2)
    elif num == "quit":
        print("Exit")
        break
    else:
        print("Wrong Input!")
        continue
