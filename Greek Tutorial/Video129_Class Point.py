# exercise 4: Points Class
class Point:
    def __init__(self,x,y):
        self.__x = x 
        self.__y = y
        
    def set_x(self,x):
        self.__x = x 
    
    def set_y(self,y):
        self.__y = y 
            
    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
        
def f(x):
    return x**2
 
# 1st way       
points = []
for x in range(1,11):
    p = Point(x,f(x))
    points.append(p)

for point in points:
    print(f"({point.get_x()},{point.get_y()})")

 
# 2nd way
points = [Point(0,0) for _ in range(10)]

i = 1 
for point in points:
    point.set_x(i)
    point.set_y(i*i)
    
for point in points:
    print(f"({point.get_x()},{point.get_y()})")
