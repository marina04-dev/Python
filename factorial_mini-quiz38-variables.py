#factorial_function
def fact(number):
    result = 1
    for i in range(1,number+1):
       result *= i
   return result
    
#mini-quiz-38-variables(topics-catholics)    
def minus_one(value):
    number = 1
    value += number
    return value
    
number = 10

def add_numbers(value, value2):
    number = 5
    minus_one(number)
    return value + value2 - number
    
print(number)
print(add_numbers(3, 5))
print(minus_one(minus_one(number)))
print(add_numbers(5, minus_one(number)))


