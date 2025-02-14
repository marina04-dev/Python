from abc import ABC, abstractmethod
from math import pi

class GeometricObjectInterface(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Circle(GeometricObjectInterface):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return pi*(self.radius**2)
    
    def perimeter(self):
        return 2 * pi * self.radius
    
class Resizable(ABC):
    @abstractmethod
    def resize(self, param):
        pass
    
class ResizableCircle(Circle,Resizable):
    def __init__(self, radius):
        Circle.__init__(self, radius)
        
    def resize(self, param):
        self.radius = self.radius * param
        
        
c = ResizableCircle(3)
print(c.area(), c.perimeter())
c.resize(4)
print(c.area(), c.perimeter())
