from date import Date
from assignment import Assignment

def main():
    newdate = Assignment()    
    Assignment.prompt(newdate)
    Assignment.printday(newdate)

if __name__ == "__main__":
    main()