# Numbers Summary (while-loop)
# exercise 2 (while)
i=0
my_list = 0
while i<10:
    num = input("Enter a number: ")
    if num.isdigit():
        my_list += int(num)
        i += 1
        print(my_list)
    else:
        print("Wrong Input!")
        continue
