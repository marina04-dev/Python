# Numbers sorting (list version) - float conversion
# This program does not work with float input
# Exercise 2 (Lists)
while True:
    item1 = input("Enter the 1st number: ").strip()
    item2 = input("Enter the 2nd number: ").strip()
    item3 = input("Enter the 3rd number: ").strip()
    my_list = []
    if item1.isdigit() and item2.isdigit() and item3.isdigit():
        new_item1 = int(item1)
        my_list.append(new_item1)
        new_item2 = int(item2)
        my_list.append(new_item2)
        new_item3 = int(item3)
        my_list.append(new_item3)
        my_list.sort()
        print(my_list)
        break
    else:
        print("Wrong Input! Please enter only digits!")
        continue
    
