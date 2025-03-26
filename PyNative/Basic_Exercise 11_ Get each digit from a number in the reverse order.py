"""Exercise 11: Get each digit from a number in the reverse order."""
"""For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits."""
def rev(number):
    while number > 0:
        # get the last digit 
        digit = number % 10
        # remove the last digit and repeat the loop
        number = number // 10
        print(digit, end=" ")
        
rev(1234567)
