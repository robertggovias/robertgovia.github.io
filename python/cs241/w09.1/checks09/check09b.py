class NegativeNumberError(Exception):
    pass
#def __init__(self):
#        super().__init__()

def get_inverse(n):
    total = 1/n
    if total < 0:
        raise NegativeNumberError("Error: The value cannot be negative")
    
    return total
                
def main():
    try:
        result = get_inverse(int(input("Enter a number: ")))
        print("The result is: {}".format(result))
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except ValueError:
        print("Error: The value cannot be negative")
    except NegativeNumberError as e:
        print(e.args[0])
if __name__ == "__main__":
    main()
