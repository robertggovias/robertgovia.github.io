class Person:
    def __init__(self):
        self.name = "anonymous"        
        self.year = "unknown"
    '''def gname(self):
        return self.name
    def gyear(self):
        return self.year'''
    def display(self):
        print("Author:\n{} (b. {})".format(self.name,self.year))
class Book:
    def Person(self,name,year):
        self.name = name
        self.year = year
    def gname(self):
        return self.name
    def gyear(self):
        return self.year

    def __init__(self):
        self.title = "untitled"        
        self.publisher = "unpublished" 
        self.name =  gname(self)
        self.year =  gyear(self)

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
