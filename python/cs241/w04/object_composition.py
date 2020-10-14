class Person:
    def __init__(self, name, year):
        self.name = "anonymous"        
        self.year = "unknown"
    def gname(self):
        return self.name
    def gyear(self):
        return self.year
    def display(self):
        print("Author:\n{} (b. {})".format(self.name,self.year))
class Book:
    
    def __init__(self, name,year):
        self.title = "untitled"        
        self.publisher = "unpublished" 
        self.name =  Person(name,year)
    def gtitle(self):
        return self.title
    def gpublisher(self):
        return self.publisher
    
    def display(self):        
        print("{}\nPublisher:\n{}".format(self.title,self.publisher))
        Person.display(self)
        #print("{} (b. {})".format(self.name,self.year))
newA = Book()
Book.display(newA)
newA = Person()
Person.display(newA)

newB = Book()
newB = Person()

newB.title = "The Great Divorce"
newB.publisher = "Geoffrey Bles"
newB.name= "C.S. Lewis"
newB.year = "1898"
Book.display(newB)
