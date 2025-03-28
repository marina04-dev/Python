# ---------------- UNIT 5: Classic Algorithms ---------------------- #
# ---------------- Activity 5 ---------------------- #
# write a function that will take a list with boolean values
# and it will place first the true values and after the false

# 1st way: Simply count the true then substrack from list's length
# we find the false.We arrange the true's to the first k values at first
# places and then the false
def count_true_values(booleanList):
    true_values = 0
    for item in booleanList:
        if item:
            true_values = true_values + 1
    return true_values

def count_true_values2(booleanList):
    true_values = 0
    for item in booleanList:
        true_values = true_values + item
    return true_values

# 1st solution: count true values and then put that amount of
# true values in array's/list's places and to the others false
def swap_boolean_by_counting(List):
    N = len(List)
    true_values = count_true_values(List)
    for i in range(true_values):
        List[i] = True
    for i in range(true_values, N):
        List[i] = False
    return List


# 2nd solution: we start with 2 pointers in the edges of the list
# and we switch the different elements(True, False) until we meet
# on the left False or from the right True. Pointers move at the same time
# and at the opposite position. When they meet the function stops
def swap_boolean_by_comparison(List):
    N = len(List)
    left = 0
    right = N-1
    while left < right:
        if List[right] == True and List[left] == False:
            List[left], List[right] = List[right], List[left]
            left = left + 1
            right = right - 1
        elif List[right] == False:
            right = right - 1
        else:
            left = left + 1
    return List

