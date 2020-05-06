def prompt_file():
    x = input("Please enter the data file: ")
    return x
def parse(x):
    y=open(x,"r")
    p=y.readlines()
    return p
def printLine(x,y):
    f=print(x[y])
    return f

def splitPrint(x,y,z):    
    p=x[y].split(",")
    f=(p[z])
    for i in f:
        
    '''for i in x[y]:
        z = i.split(",")
    e=print(z)
    #f=print("{} ({}, {}) - ${}".format(z[2],z[0],z[3],z[6]))'''
    return f

def main():
    x = parse(prompt_file())
    #y = printLine(x,2,2)
    y = print(list(range(splitPrint(x,1,6),splitPrint(x,5,6))))
    return y
if __name__ == "__main__":
    main()