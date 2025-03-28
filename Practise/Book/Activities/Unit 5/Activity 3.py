# ---------------- UNIT 5: Classic Algorithms ---------------------- #
# ---------------- Activity 3 ---------------------- #
# write a function that will accept as argument a list, it will check if
# list's elements are sorted in ascending order and it will return true or false in either way
# write one version with a boolean variable and one without

''' with Boolean variable version '''
def is_ascending(mylist):
    ascending = True
    i = 0
    N = len(mylist)
    while ascending and i<N-1:
        if mylist[i] > mylist[i+1]:
            ascending = False
        i = i + 1
    return ascending

''' without Boolean variable version '''
def is_ascending2(mylist):
    i = 0
    pred = mylist[0]
    for item in mylist:
        if item < pred:
            return False
        else:
            pred = item
    return True
