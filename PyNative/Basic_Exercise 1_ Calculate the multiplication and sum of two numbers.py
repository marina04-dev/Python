"""Exercise 1: Calculate the multiplication and sum of two numbers"""
"""Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum."""
def multiplication_or_sum(num1, num2):
    # calculate product of the two numbers
    product = num1 * num2
    # check if product is less than 1000
    if product <= 1000:
        return product
    else:
        # product is greater that 1000 calculate sum 
        return num1 + num2
