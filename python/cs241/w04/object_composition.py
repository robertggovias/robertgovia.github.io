class Person:
    def __init__(self):
        self.name = "anonymous"        
        self.year = "unknown"
    def display(self):
        print("{} (b. {})".format(self.name,self.year))
class Book:
    def __init__(self):
        self.title = "untitled"        
        self.publisher = "unpublished"
        self.name = Person()
        self.year = Person()        

    def display(self):        
        print("{}\nPublisher:\n{}".format(self.title,self.publisher))
        print("{} (b. {})".format(self.name,self.year))

print()
newB = Book()
newB.title = "The Great Divorce"
newB.publisher = "Geoffrey Bles"
newB.name= "C.S. Lewis"
newB.year = "1898"
#Person.display(new)
Book.display(newB)

