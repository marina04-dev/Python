# 2 Dimensions Lists - Lesson 6: Exercise 6
array = []
while (True):
    rows = input("Enter the number of rows or 0 to exit: ").strip()
    cols = input("Enter the number of columns: ").strip()
    if (rows.isdigit() and cols.isdigit()):
        row = int(rows)
        col = int(cols)
        if row == 0 or col == 0:
            break
        elif row<0 or col<0:
            print("Please enter a number bigger than 0!")
            continue
        else:
            for i in range(row):
                array.append([])
                for j in range(col):
                    elem=input(f"Enter the {i},{j} element: ")
                    if elem.isdigit():
                        element = int(elem)
                        array[i].append(elem)
            print(array)
            break
    else:
        print("Enter only digits please!")
