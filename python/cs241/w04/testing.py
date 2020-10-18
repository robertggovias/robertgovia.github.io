class Address:
    def __init__(self):
        self.name="street"
        self.city="city"
    #def display(self):
        #print(self.name)

    

class Person:
    def __init__(self):
        self.first_name = "name"
        self.last_name = "lastname"
        self.author = Address()
        self.work = Address()
    
    def display(self):
        print(self.author.name)
    

bob = Person()
#bob = Address()
print(bob.author.name)
Person.display(bob)
#Address.display(bob)

bob.author.name = "creole"

print(bob.author.name)

