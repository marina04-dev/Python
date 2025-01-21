def calculations(first, second, operator='+'):
    if operator=='+':
        return first+second
    if operator=='-':
        return first-second
    if operator=='*':
        return first*second
    if operator=='/':
        return first/second
    if operator=='%':
        return first%second
    if operator=='**':
        return first**second
        
print(calculations(4,3))
print(calculations(4,3,'-'))
print(calculations(4,3,'*'))
