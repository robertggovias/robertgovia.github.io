class Person:
    #def __init__(self, name, year):
    def __init__(self):
        self.name = "anonymous"        
        self.year = "unknown"
        #self.author = self.name, self.year
            
    def display(self):
        self.author = print("Author:\n{} (b. {})".format(self.name,self.year))
       # print("Author:\n{} (b. {})".format(self.author(name,year))
       #print("Author:\n{} (b. {})\n".format(self.name,self.year))
        

class Book:
    
    def __init__(self):
        self.title = "untitled" 
        self.publisher = "unpublished"
        self.author = Person()

    def display(self):        
        print("{}\nPublisher:\n{}".format(self.title,self.publisher))
        self.author.display()
        #print("Author:\n{} (b. {})".format(self.author.name,self.author.year))        

def main():
    newA = Book()
    Book.display(newA)
    print()
    print("Please enter the following:")
    newA.author.name= input("Name: ")
    newA.author.year = input("Year: ")
    newA.title = input("Title: ")
    newA.publisher = input("Publisher: ")
    print()
    Book.display(newA)

if __name__ == "__main__":
    main()
