from date import Date

class Assignment():
    def __init__(self):
        """
        docstring
        """
        self.name = str("Untitled")        
        self.start_date = Date()
        self.due_date = Date()
        self.end_date = Date()
    
    def display(self):
        print("\nstart day:")
        self.start_date.display()
        print("\ndue day:")
        self.due_date.display()
        print("\nend day:")
        self.end_date.display()        
    
    def prompt(self):
        self.name = str(input("Name: "))
        print("\nStart day: ")
        self.start_date.prompt()
        print("\nDue day: ")
        self.due_date.prompt()
        print("\nEnd day: ")
        self.end_date.prompt()  
    
    def printday(self):
        print("\nstart day:")
        self.start_date.display()
        print("\ndue day:")
        self.due_date.display()
        print("\nend day:")
        self.end_date.display()      