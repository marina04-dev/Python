#Memory_Game_With_Cards
array = [1,3,2,4,3,2,1,4]
elem = 8
while(elem>0):
    pick_1 = int(input(f"Give a number between 0 and "+str(elem-1)+": "))
    pick_2 = int(input(f"Give another number between 0 and "+str(elem-1)+": "))
    if array[pick_1]==array[pick_2]:
        print("Same")
        array.pop(pick_1)
        array.pop(pick_2)
        elem = elem-2
    else:
        print("Different")
