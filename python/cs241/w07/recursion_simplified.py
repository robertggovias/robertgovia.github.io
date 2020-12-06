def recursive(num):

    if num <= 0:
        return

    print("function result : {}".format(num))    
    recursive(num-1)
    


def main():
    f = int(input("put a number to creat reusiveness (function inside a function): "))
    recursive(f)

if __name__ == "__main__":
    main()