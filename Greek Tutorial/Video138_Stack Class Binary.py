# Lesson 16: Exercise 13 - Stack Class - Binary Representation
class Stack:
    def __init__(self):
        self.array = []
    def push(self,elem):
        self.array.append(elem)
    def pop(elem):
        if not self.array:
            return None 
        else:
            return self.array.pop()
    def length(self):
        return len(self.array)
        
def binary(n):
    st = Stack()
    while n > 0:
        st.push(n%2)
        n = n//2
        
    res = []
    while (st.length() > 0):
        res.append(str(st.pop()))
    return "".join(res)
    print(res)
        
for i in range(300):
    print(binary(i))
