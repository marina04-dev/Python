# ----------------- Unit 5: Classic Algorithms ------ #
# ---------------- Activity 9 ---------------------- #
# write a function which will read numbers from the user and it will
# place them in a list in descending order and it will then return 
# the list. Each time it will read a number, it will place it in 
# the right position of the already sorted list, so that it maintains
# the descending order of list's elements. The reading stops when 
# value `None` is given.

# Solution: we need a sorting algorithm which will gradually sort 
# a slice of the array (incremental). We don't want each time 
# we read a number to sort again all the array, but to place the 
# element in the right position, so that the array remains sorted.
# We will use the insertion sort algorithm.
def insertion_sort():
    print("Enter value `None` to stop")
    number = input("Enter a number: ")
    L = []
    while number != "None":
        number = int(number)
        L.append(number)
        value = L[len(L)-1]
        j = len(L) -1 
        while j>0 and L[j-1]<value:
            L[j]=L[j-1]
            j=j-1
        L[j]=value
        number=input("Enter a number: ")
    return L 
    
print(insertion_sort())
