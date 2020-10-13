class Complex:


    '''def __init__(self, numerator, denominator):
        self.n = numerator
        self.d = denominator'''
    
    def __init__(self):
        self.n = 0
        self.d = 0


    def display(self):
        print ("{}/{}".format(self.n, self.d))
        #print(str(self.n) + "/" + str(self.d))
    
    def prompt(self):
        self.n = input("Enter the numerator: ")
        self.d = input("Enter the denominator: ")
    
    def display_decimal(self):
        f = int(self.n) / int(self.d)
        print(f)
        
def main():
    
    c1 = Complex()
    #c1 = Complex(0,1)    
    c1.display()
    c1.prompt()
    
    c1.display_decimal()

    

# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()