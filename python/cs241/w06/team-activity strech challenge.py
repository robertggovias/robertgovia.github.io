class Point:
    def __init__(self):
        self.x = 0.00
        self.y = 0.00

    def prompt_for_point(self):
        self.x=float(input(("Enter x:")))
        self.y=float(input(("Enter y:")))
        

    def display(self):
        print("Center: ({}, {})".format(self.x,self.y))

class Circle():
    def __init__(self):
        self.radius=0.00      
        self.center=Point() 

    def prompt_for_circle(self):
        self.center.prompt_for_point()
        self.radius=input("Enter radius:")

        self.center.x=5345
        self.center.y=5345

        
    def display(self):
        self.center.display()
        print("\nRadius: {}".format(self.radius))        

def main():    
    new_circle=Circle()
    new_circle.display()
    new_circle.prompt_for_circle()
    new_circle.display()

if __name__ == "__main__":
    main()



