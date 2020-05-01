def prompt_number():
    x = -1
    while x < 0:
        x = int(input("Enter a positive number: "))
        if x < 0:
            print("Invalid entry. The number must be positive.")
    return x

def compute_sum(a,b,c):
    sum = a + b + c
    return sum

def main():
    a = prompt_number()
    print()
    b = prompt_number()
    print()
    c = prompt_number()    
    print()
    d = compute_sum(a,b,c)
    print("The sum is: {}".format(d))
    return d

if __name__ == "__main__":
    main()