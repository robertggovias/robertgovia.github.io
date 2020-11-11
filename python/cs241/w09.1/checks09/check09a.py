x = False

while not x:
    try:
        x = int(input("Enter a number: "))
        result = x * 2
        print("The result is: ",result)
    except ValueError:
        print("The value entered is not valid")

