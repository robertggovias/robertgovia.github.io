class Point:
    def __init__(self):
        self.x = 0.00
        self.y = 0.00

    def prompt_for_point(self):
        self.x=float(input(("Enter x:")))
        self.y=float(input(("Enter y:")))
        
    def display(self):
        print("Center: ({}, {})".format(self.x,self.y))        

class Circle(Point):
    def __init__(self):
        self.radius=0.00      
        super().__init__()        

    def prompt_for_circle(self):
        self.prompt_for_point()        
        self.radius=input("Enter radius:")
        
    def display(self):
        super(Circle,self).display()
        print("\nRadius: {}".format(self.radius))
 
def main():
    
    new_circle=Circle()
    new_circle.prompt_for_circle()
    new_circle.display()

if __name__ == "__main__":
    main()