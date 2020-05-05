def prompt_file():
    x = input("Please enter the data file: ")
    return x
def parse(x):
    y=open(x,"r")
    p=y.readlines()
    return p
def printLine(x,y,z):
    f=print(x[y][z])
    return f

def splitPrint(x,y):    
    for i in x[y]:
        z = i.split(",")
    e=print(z)
    #f=print("{} ({}, {}) - ${}".format(z[2],z[0],z[3],z[6]))
    return e

def main():
    x = parse(prompt_file())
    y = printLine(x,1,2)
    #y = splitPrint(x,4)
    return y
if __name__ == "__main__":
    main()