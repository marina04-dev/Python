# exercise 4: *args and **kwargs in functions
def print_details(*args,**kwargs):
    print(kwargs)
    s = 0
    for number in args:
        s += number
    average = s/len(args)
    print(average)  
    
    dictionary = {}
    for key, value in kwargs.items():
        if value in dictionary:
            dictionary[value] += 1 
        else:
            dictionary[value] = 1
    print(dictionary)
    
print_details(5,8,13,Banner="Discrete Mathematics", Kane="Discrete Mathematics", Stark="Programming")
