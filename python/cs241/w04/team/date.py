class Date:
    def __init__(self):
        self.day = int(1)
        self.month = int(1)
        self.year = int(2000)
    
    def display (self):
        print("{}/{}/{}".format(self.day,self.month,self.year))
    
    def prompt(self):
        print("please insert the information required:")
        self.day = int(input("day: "))
        self.month = int(input("month: "))
        self.year = int(input("year: "))
        
