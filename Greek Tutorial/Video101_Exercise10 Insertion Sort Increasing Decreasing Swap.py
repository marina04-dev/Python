# insertion sort increasing
def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if (array[j]<array[j-1]):
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break
            

array=[9,2,4,7,1,8,6,3]
print(array)
insertion_sort(array)
print(array)
          
          
# insertion sort decreasing
def insertion_sort_dec(array):
    for i in range(1,len(array)):
        for j in range(i,0,-1):
            if (array[j]>array[j-1]):
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break
            

array=[9,2,4,7,1,8,6,3]
print(array)
insertion_sort_dec(array)
print(array)
            
def swap(a,b):
    tmp=a
    a=b 
    b=tmp
    return a,b
    
# example swap
a=3
b=4
print(f"a={a}, b={b}")
a,b=swap(a,b)
print(f"a={a}, b={b}")


a=3
b=4
a,b=(b,a)
print(f"a={a}, b={b}")

a=3
b=4
a,b=b,a
print(f"a={a}, b={b}")
