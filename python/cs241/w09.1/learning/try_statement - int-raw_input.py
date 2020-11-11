#n = int(input("Please enter a number: "))

while True:
    try:
        n = input("Please enter a number: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print ("Great, you successfully entered an integer!")