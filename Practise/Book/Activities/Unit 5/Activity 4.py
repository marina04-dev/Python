# ---------------- UNIT 5: Classic Algorithms ---------------------- #
# ---------------- Activity 4 ---------------------- #
# improved bubble sort algorithm: it stops when the list is completely sorted
# 1st version: with a boolean variable
def optimized_bubble_sort(A):
    N = len(A)
    is_sorted = False
    i = 1
    while i < N and not is_sorted:
        is_sorted = True
        for j in range(N-1,i-1,-1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
                is_sorted = False
        i = i+1


# 2nd version with immediate stop of for loop
def optimized_bubble_sort2(A):
    N = len(A)
    for i in range(N):
        is_sorted = True
        for j in range(N-1,i,-1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                is_sorted = False
            if is_sorted:
                return True
