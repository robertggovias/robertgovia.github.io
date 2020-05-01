def prompt_filename():
    file=input("Enter file: ")
    return file
def parse_file(x):
    book=open(x)
    count=0
    for i in book:
        z=i.split()
        for y in z:            
            if y == "pride" or y == "Pride":
                count += 1
    return count

def main():
    x=prompt_filename()
    print("Opening file {}".format(x))    
    
    y=parse_file(x)
    print("The word pride occurs {} times in this file".format(y))
    
if __name__ == "__main__":
    main()
