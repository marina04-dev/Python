# ---------------- UNIT 5: Classic Algorithms ---------------------- #
# ---------------- Activity 8 ---------------------- #
# problem of dutch flag occurs in reordering a list with
# letters which contains only characters 'R', 'W', 'B' (Red, White, Blue)
# so that all R to be before W and all W to be before B.

# Solution: we change the algorithm of immediate change
def dutch_flag(letters):
    N = len(letters)
    for i in range(N):
        for j in range(N-1, i, -1):
            if (letters[j]=='W' and letters[j-1]=='B')\
                or (letters[j]=='R' and letters[j-1]=='W')\
                or (letters[j]=='R' and letters[j-1]=='B'):
                    letters[j-1], letters[j] = letters[j], letters[j-1]
    return letters
