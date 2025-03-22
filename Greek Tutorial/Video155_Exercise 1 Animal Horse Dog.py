class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
    def __str__(self):
        return f"Weight: {self.weight}, Height: {self.height}"
        
        
class Horse(Animal):
    def __init__(self, weight, height, color, tail_width):
        super().__init__(weight, height)
        self.color = color
        self.tail_width = tail_width
        
        
class Dog(Animal):
    def __init__(self, weight, height, dB):
        super().__init__(weight, height)
        self.dB = dB
        
    def bark(self):
        print("Woof Woof!")
        
class Doberman(Dog):
    def __init__(self, weight, height, dB):
        super().__init__(weight, height, dB)
        
    def run(self):
        print("Doberman Runs!")
        
        
class Bulldog(Dog):
    def __init__(self, weight, height, dB, ear_length):
        super().__init__(weight, height, dB)
        self.ear_length = ear_length
        
    def sleep(self):
        print("Bulldog Sleeps!")
        
        
lassie = Horse(123,234,"black",76)
print(lassie.color)

bob = Doberman(123,234,67)
bob.bark()

tom = Bulldog(123,234,67,23)
tom.sleep()
