#Like @Kevin said, there will be two classes.  This is your first exposure to encapsulation, where one object has another object inside of it.  Your book object will contain a person object that represents the author of the book.
class Class1:
  def __init__(self, attribute = "Hello, world"):
    ''' This is a normal class with a single attribute '''
    self.attribute = attribute
class Class2:
  def __init__(self, attribute = Class1()):
    ''' This class has an attribute that is of type Class1 '''
    self.attribute = attribute
my_object = Class2()
print(my_object.attribute.attribute) # Print the attribute of the Class1 object contained in the attribute of the Class2 object.  This will print out "Hello, world" by default
my_object = Class2(Class1("Hello, class world")) # This makes a new Class 2 object that has a Class1 object inside of it with an attribute containing "Hello, class world"
print(my_object.attribute.attribute)
#This example might be confusing at first, especially because I called the attribute in both classes "attribute".  I did this to emphasize that there is a Class1.attribute and a Class2.attribute, and they are different things. (editado) 