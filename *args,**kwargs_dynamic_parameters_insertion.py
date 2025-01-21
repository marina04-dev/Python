def larger_number(*args, **kwargs):
    print(max(args))
    print(min(kwargs.values()) if kwargs else '-')
    
nums = larger_number(20,30,1,90,56)

#The difference between *args and **kwargs is that *args is storing values in a tuple while **kwargs is storing values in a dictionary 

#When we have default values in parameters we put them in the end of the parameters

#When we want to have keywords in the parameters we put a *, and then the parameters 
