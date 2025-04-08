# ----------------- Unit 5: Classic Algorithms ------ #
# ---------------- Activity 4: Exercise Book ----------------- #
# write a program which, will read names, until name '0' is given
# and it will return them in alphabetical order. Extension: Then 
# the program will read a name and it will show appropriate message
# if the name is in the names list or not 

# Solution: We will use binarySearch and bubbleSort functions
def bubble_sort(mylist):
    N = len(mylist)
    for i in range(N):
        for j in range(N-1, i, -1):
            if mylist[j] < mylist[j-1]:
                mylist[j], mylist[j-1] = mylist[j-1], mylist[j]
                

def binary_search(mylist, key):
    last = len(mylist) -1
    first = 0 
    found = False 
    while first <= last and not found:
        mid = (last+first)//2
        if mylist[mid] == key:
            found = True 
        elif mylist[mid] < key:
            first = mid+1 
        else:
            last = mid-1 
    return found 
    
    
name = input("Enter name: ")
nameList = []
while name != '0':
    nameList.append(name)
    name = input("Enter name: ")
    
bubble_sort(nameList)
name = input("Enter name to search: ")
found = binary_search(nameList, name)
if found >= 0:
    print("Name was found in the list")
else:
    print("Name was not found in the list")
