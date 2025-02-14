from random import randrange, seed
from datetime import datetime


class Node:
    def __init__(self, data, nnext=None):
        self.nnext = nnext
        self.data = data
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def empty(self):
        return self.head is None 
    
    def insert_start(self,data):
        n = Node(data)
        n.nnext = self.head
        self.head = n 
        
    def insert_after(self, prev, data):
        n = Node(data)
        n.nnext = prev.nnext
        prev.nnext = n 
        
    def delete_start(self):
        if self.empty():
            return None
        else :
            current = self.head
            self.head  = self.head.nnext
            return current.data
        
    def delete_after(self, prev):
        if prev.nnext is None:
            return None
        else:
            c = prev.nnext
            prev.nnext = c.nnext
            return c.data
            
    def __str__(self):
        p = self.head
        st = ""
        while p is not None:
            st += str(p.data) + " --> "
            p = p.nnext
        st += "."
        return st 
        
        
class OrderedList(LinkedList):
    def __init__(self):
        super().__init__()
        
    def insert(self, data):
        if self.empty():
            self.insert_start(data)
        elif data < self.head.data:
            self.insert_start(data)
        else:
            prev = self.head
            cur = self.head.nnext
            while cur is not None:
                if data < cur.data:
                    self.insert_after(prev,data)
                    return
                else:
                    prev = cur 
                    cur = cur.nnext
            else:
                self.insert_after(prev, data)
                
    def delete(self, data):
        if self.empty():
            return None 
        elif self.head.data == data:
            return self.delete_start()
        else:
            prev = self.head
            cur = self.head.nnext
            while cur is not None:
                if data == cur.data:
                    return self.delete_after(prev)
                else:
                    prev = cur 
                    cur = cur.nnext
            else:
                return None
    
    

l = LinkedList()
for i in range(4,-1,-1):
    l.insert_start(i)
print(l)
       
l.insert_after(l.head.nnext.nnext, 5) 
print(l)
print(l.delete_start())
print(l)
print(l.delete_after(l.head.nnext))
print(l)

print("-" * 35)
seed(datetime.now())
ol = OrderedList()
for i in range(50):
    val = randrange(10)
    if i%2 == 0:
        ol.insert(val)
        print(f"Inserted {val}.")
    else:
        ret = ol.delete(val)
        if ret is None:
            print(f"Deleting... {val} not found!")
        else:
            print(f"Deleted {val}.")
        
