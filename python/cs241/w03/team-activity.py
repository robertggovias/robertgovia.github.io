class Complex:
    def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator
    
    def display(self):
        print(str(self.n) + "/" + str(self.d))
    
    def prompt(self):
        self.n = input("Enter the numerator: ")
        self.d = input("Enter the denominator: ")
    
    def display_decimal(self):
        return int(self.n / self.d)
        
def main():
    """
    This function tests your Complex class. It should have a prompt
    and a display member function to be called.

    You should not need to change this main function at all.
    """
    c1 = Complex(0,1)    
    c2 = Complex(0,1)    
        
    c1.display()

    print()
    c2.prompt()

    c2.display()

    c2.display_decimal()

# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()