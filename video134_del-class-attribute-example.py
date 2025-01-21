# Class Attribute: example
class C:
    counter = 0
    def __init__(self):
        C.counter += 1
        
o1 = C()
o2 = C()
print(C.counter, o1.counter, o2.counter)

# Del : example
class C:
    def __init__(self):
        C.c += 1 
    def __del__(self):
        C.c -= 1
        
o1 = C()
o2 = C()
print(o1.C)
del o1
print(o2.c)
