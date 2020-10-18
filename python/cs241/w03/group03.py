import math

class Rational_Number():    
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
    
    def __repr__(self):
        result = self.numerator + "/" + self.denominator
        #if result:
    
    def prompt(self):

        self.numerator = int(input("Enter the Numerator: "))
        self.denominator = int(input("Enter the Denominator: "))
    
    def display_decimal(self):
        return str(float(self.numerator / ))
        
else
    return_string = f"{str(self.numerator)}/{str(self.denominator)}"
return return_string

def main():
    Test_1 = Rational_Number()
    print(Test_1)

    Test_2 = Rational_Number()
    Test_2.get_ratio()
    print(Test_2)
    print(Test_2.display_decimal())
"""Test_1= Ratio(5,7)

print(Test_1)"""

main()