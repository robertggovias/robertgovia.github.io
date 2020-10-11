even = []
odd = []

number = int(input("Enter a number (0 to quit):"))
while number > 0:
    if int(number)%2 == 0:
        even.append(number)
    else:
        odd.append(number)
    number = int(input("Enter a number (0 to quit):"))

print("\nEven numbers:")
for ev in even:
    print(ev)
print("\nOdd numbers:",)
for od in odd:
    print(od)