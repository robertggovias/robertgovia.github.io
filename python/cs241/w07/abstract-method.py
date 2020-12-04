from abc import ABC, abstractclassmethod
class Shape(ABC):
    

    @abstractclassmethod
    def area(self): pass

    @abstractclassmethod
    def perimeter(self):pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side

square = Square(5)
print(square.area())
print(square.perimeter())