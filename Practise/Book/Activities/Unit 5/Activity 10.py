# ----------------- Unit 5: Classic Algorithms ------ #
# ---------------- Activity 10 ---------------------- #
# write a function which will read 2 numeric lists from the user 
# and it will sort the numbers from the first list in ascending 
# order and then it will find which numbers from first list are also found 
# in the second list. Assume that all numbers from the second list 
# are different.

# Solution: First we use the readList function from activity 6.
# Then we apply a sorting algorithm so that we can then use binary search
# to check if any element from the first list is also in the second list.

def readList():
    print("*****************************************")
    print("For the end give the value None")
    print("*****************************************")
    index = 0
    L = []
    value = input("L[" + str(index) + "] = ")
    while value != "None":
        L.append(value)
        index += 1
        value = input("L[" + str(index) + "] = ")
    return L


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
    
    
def final_function():
    A = readList()
    B = readList()
    bubble_sort(A)
    count = 0 
    for item in B:
        if binary_search(A, item):
            count = count + 1 
    print("Number of same items = ", count)
    
final_function()
        
    
