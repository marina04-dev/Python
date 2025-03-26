# Numbers Sorting - List Version
# Exercise 8 (while)
num = input("Enter a number between 3 and 20: ").strip()
my_list = []
if num.isdigit:
    nums = int(num)
    while len(my_list) < nums:
        n = input("Enter a number: ").strip()
        if n.isdigit():
            z = int(n)
            my_list.append(z)
            my_list.sort()
        else:
            print("Enter only digits please!")
            continue
else:
    print("Enter only digits!")
        
print(my_list)
