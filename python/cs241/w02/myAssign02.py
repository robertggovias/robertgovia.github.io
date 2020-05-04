def prompt_file():
    x = input("Please enter the data file: ")
    return x
def parse(x):
    y=open(x,"r")
    p=y.readlines()    
    return p

def main():
    x = parse(prompt_file())
    print(x[3])
    return x
if __name__ == "__main__":
    main()