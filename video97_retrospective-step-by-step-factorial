# explanation of retrospective: step-by-step factorial
def factorial(n):
    print((5-n) * "\t" + "Call factorial(" + str(n) + ")")
    if n == 1:
        print((5-n+1) * "\t" + "return 1")
        return 1 
    else:
        print((5-n+1) * "\t" + "return " + str(n) + "*factorial(" + str(n-1) + ")")
        fact = factorial(n-1)
        res = n*fact 
        print((5-n+1) * "\t" + "return " + str(n) + "*" + str(fact))
        return res
            
            
factorial(5)


explanation: step-by-step
+==============+        +==============+     +==============+      +==============+     +==============+ 
| factorial(5) | -----> | factorial(4) | --> | factorial(3) | ---> | factorial(2) | --> | factorial(1) |
|    5*24      | <----- |     4*6      | <-- |     3*2      | <--- |       2*1    | <-- |      1       |
+==============+        +==============+     +==============+      +==============+     +==============+
