N = 25
calls = 0

def fibonacci(n):
    global calls
    calls += 1

    if n == 0:
        print(N * "\t" + "return 0")
        return 0
    elif n == 1:
        print(N * "\t" + "return 1")
        return 1
    else:
        print((N - n + 1) * "\t" + "CALL fibonacci(" + str(n - 1) + ")")
        prevprev = fibonacci(n-1)
        print((N - n + 1) * "\t" + "CALL fibonacci(" + str(n - 2) + ")")
        prev = fibonacci(n-2)
        print((N - n + 1) * "\t" + "return " + str(prev) + " + " + str(prevprev))
        return prevprev + prev

fibonacci(N)
print(f"calls = {calls}")

# fibonacci.py
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(11):
    print(f"fibonacci({i})={fibonacci(i)}")
