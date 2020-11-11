class NegativeNumberError(Exception):
    def __init__(self,message):
        super().__init__(message)

def get_inverse():    
    try:    
        number = float(input("Enter a number: "))
        if number < 0:
            raise NegativeNumberError("Error: The value cannot be negative")
        return 1 / number
        
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    
    """except not
        print("Error: The value cannot be negative")"""        
    




def main():
    hey = get_inverse()
    print("The result is: {}".format(hey))
if __name__ == "__main__":
    main()
