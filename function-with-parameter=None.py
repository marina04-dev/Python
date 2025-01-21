def larger_number(number1, number2, number3 = None):
    max_number = number1
    if number2>max_number and number2>number3:
        max_number = number2
    elif number3>max_number and number3>number2:
        max_number = number3
    print(max_number)
    
values = larger_number(5,7,9)
