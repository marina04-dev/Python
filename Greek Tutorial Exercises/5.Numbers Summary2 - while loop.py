# Numbers Summary: while loop (list-version)
# Exercise 3 (while)
i=0
my_list = []
summary = 0
while i<10:
    num = input("Enter a number: ")
    if num.isdigit():
        my_num = int(num)
        my_list.append(my_num)
        summary += my_list[i]
        i += 1 
    else:
        print("Wrong Input!")
        continue
print(my_list)
print(summary)
