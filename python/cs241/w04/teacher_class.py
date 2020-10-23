class ExampleClass:
    def __init__(self):
        self.name = "Robert"
        self.numero = 2
        self.lists = (1,2,3)
    
    def display(self):
        print(self.name,self.numero,self.lists)
    
class ExampleIn():
    def __init__(self,why = "isn't your business",where = 2324,when = [22,11,1982]):
        self.why = why
        self.where = where
        self.when = when
    
    def set_where(self,where):
        self.where = where
    
    def set_when(self):
        return self.when
    def display(self):
        print(self.why,self.where,self.when)
    def hello_world():
        print("print hello")
if __name__ == "__main__":
    example_object = ExampleClass()  #Create a new Object

    example_object.number = 5 
    example_object.text = "hello" 
    example_object.list = [1,2,3] 
    print(example_object.number,example_object.text,example_object.list)
    oi = ExampleClass()
    print(oi.lists,oi.name, oi.numero)
    example_object = ExampleIn()
    example_object.display()
    print(dir(example_object))

    example_object = ExampleIn([24234,"frse",432423,3424,"fre",123],4,3)
    example_object.display()
    example_object.set_where("Eternal Family")
    example_object.display()
    example_object.where = "Eternal Success"
    example_object.display()
    ExampleIn.set_where(example_object, "today")
    ExampleIn.display(example_object)
    ExampleIn.hello_world()