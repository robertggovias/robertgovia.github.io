class Complex:
    def __init__(self, real, imaginary):
        self.r_number = real
        self.i_number = imaginary
    
    def display(self):
        print(str(self.r_number) + " + " + str(self.i_number) + "i")
    
    def prompt(self):
        self.r_number = input("Please enter the real part: ")
        self.i_number = input("Please enter the imaginary part: ")
        
def main():
    """
    This function tests your Complex class. It should have a prompt
    and a display member function to be called.

    You should not need to change this main function at all.
    """
    c1 = Complex(0,0)
    c2 = Complex(0,0)

    print("The values are:")
    c1.display()
    c2.display()

    print()
    c1.prompt()

    print()
    c2.prompt()

    print("\nThe values are:")
    c1.display()
    c2.display()

# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()