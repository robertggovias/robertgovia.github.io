"""
Demonstrates abstract base classes.
"""
#TODO: Import anything you need for Abstract Base Classs / methods
from abc import ABC, abstractclassmethod

#TODO: convert this to an ABC

class Shape(ABC):
    def __init__(self):
        self.name = ""    
    
    def display(self):
        print("{} - {:.2f}".format(self.name, self.get_area()))        

    #TODO: Add an abstractmethod here called get_area

    @abstractclassmethod
    def get_area(self):        
        pass
        

#TODO: Create a Circle class here that derives from Shape
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Circle"
        self.radius = 0.00
    
    def get_area(self):
        return self.radius * self.radius *  3.14



#TODO: Create a Tectangle class here that derives from Shape

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "Rectangle"
        self.length = 0.00
        self.width = 0.00

    def get_area(self):
        return float(self.length * self.width)

def main():

    #TODO: Declare your list of shapes here
    shapes = []            
    command  = ""    

    while command != "q":
        command = input("Please enter 'c' for circle, 'r' for rectangle or 'q' to quit: ")
        if command == "c":
            radius = float(input("Enter the radius: "))
            #TODO: Declare your Circle here, set its radius, and
            # add it to the list
            circle = Circle()
            circle.radius =radius            
            shapes.append(circle)

    

        elif command == "r":
            length = float(input("Enter the lenght: "))
            width = float(input("Enter the widht: "))
            #TODO: Declare your Rectangle here, set its lenght
            # and width, and add it to the list
            rectangle = Rectangle()
            rectangle.length = length
            rectangle.width = width            
            shapes.append(rectangle)

        # Done entering shapes, now lets print them all out:        

        #TODO: Loop through each shape in the list, and call its display function

    for shape in shapes:
        shape.display()
    
if __name__ == "__main__":
    main()
