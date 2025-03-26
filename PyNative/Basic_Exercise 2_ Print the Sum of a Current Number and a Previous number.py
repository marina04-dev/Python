"""Exercise 2: Print the Sum of a Current Number and a Previous number"""
"""Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number."""
previous_num = 0 
for i in range(1,11):
    x_sum = previous_num + i  
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    previous_num = i 
