# exercise 5_eukleidios-algorithms
def euk(a,b):
    if (a==b):
        return a
    elif (a<b):
        return euk(a,b-a)
    else:
        return euk(a-b,b)
    
print(euk(6,9))

# exercise 6_list
def print_list(l):
    if len(l)>0:
        print(l[0],end=" ")
        print_list(l[1:])
        
print_list([1,2,3])

def print_list2(l):
    if len(l)>0:
        print_list2(l[1:])
        print(l[0],end=" ")
        
print_list2([1,2,3])


# exercise 7
def c(n,k):
    if (n==k):
        return 1 
    elif (k==1):
        return n 
    else:
        return c(n-1,k-1) + c(n-1,k)
        
print(c(49,6))
