# ---------------- UNIT 5: Classic Algorithms ---------------------- #
# ---------------- Activity 6 ---------------------- #
# write a function that will take a list with boolean values
# and it will place first the true values and after the false
# using the function from Activity 5 and then it will place them
# alternately with the minimum possible comparisons

# Solution: First we make a function that will read a list until
# value None appears. Then we make a function which will counts the
# True values, we double the amount of them and we compare it
# to the amount of list's elements. That way we find which value
# appears the least. This will be the amount of pairs (True, False)
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


def program6_counting():
    List = readList()
    N = len(List)

    # counts the true values
    true_values = count_true_values(List)

    # check if true values are more than false values
    if 2*true_values < N:
        minValue = True
        couples = true_values
    else:
        minValue = False
        couples = N - true_values

    for i in range(0, 2*couples, 2):
        List[i] = True
        List[i+1] = False

    for i in range(2*couples, N):
        List[i] = not minValue
    return List

print(program6_counting())
