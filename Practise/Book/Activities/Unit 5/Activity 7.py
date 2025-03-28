# ---------------- UNIT 5: Classic Algorithms ---------------------- #
# ---------------- Activity 7 ---------------------- #
# assume that we have a list with boolean values where the false
# values are the same amount with the true values. Write an algorithm
# which will places the True values in front of false doing the least
# possible movements. It is not allowed to do comparisons or use if
# statement. Assume that the first item of the list has the value of True.


# Solution 1: while the true values = false values in amount
# we place the half values with true and the other half with false
def  split_boolean_by_counting(mylist):
    mid = len(mylist) / 2
    for index in range(mid):
        mylist[index] = True
        mylist[index+ mid] = False
    return mylist

# Solution 2: we can pass 2 times the sorting algorithm
def split_boolean_by_sorting(mylist):
    N = len(mylist)
    mid = N/2
    for i in range(mid):
        for j in range(N-1, i,-1):
            if mylist[j] > mylist[j-1]:
                mylist[j-1], mylist[j] = mylist[j], mylist[j-1]
    return mylist

