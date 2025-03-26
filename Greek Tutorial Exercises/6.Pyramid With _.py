# Pyramid with *
# Lesson 6: Exercise 2

N = 5
for i in range(N):
    print("  " * (N-i-1), end="")
    print("* " * (2*i+1), end="")
    print("")
