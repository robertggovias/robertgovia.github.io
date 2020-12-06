
def fib(n):
    
    fib_list = [0,1,1]    

    if n < 0:
        return  
    
    if n >= 0 and n < 3:
        return fib_list[n]
    
    for  i in range (3, n+1):
        g = fib_list[i - 1] + fib_list[i - 2]    
        fib_list.append(g)           
    
    return fib_list[n]
    

def main():
    
    f = int(input("Enter a Fibonacci index:"))
    print("The Fibonacci number is: {}".format(fib(f)))    
    

if __name__ == "__main__":
    main()
