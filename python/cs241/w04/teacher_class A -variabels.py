class A:
    def __init__(self,a,b,c=0.00):
        self.first =  a
        self.second =  b
        self.price =  c

class B:
    def __init__(self):
        self.first = "B"
        self.wse = A(4,4,4)
        self.second = A(wse())
    
    #def price(self):
    #   print(self.second.price)

        # create a list as object
        '''
        self.second = [A(),A()]
        '''
    #nomal inheritance
    def display(self):
        print(self.first, self.second.first, self.second.second,self.second.price)
'''
    #list inheritance
    def display(self):
        print(self.second[0].first, self.second[1].second,self.second[1].first, self.second[1].second)
'''
if __name__ == "__main__":
    object = B()
    print("first display everyone")
    object.display()
    print("accessing B first object")
    print(object.first)

    print("accessing A first, and second object")
    print(object.second.first, object.second.second)    
    
    print("accessing B first list")
    #append to a pre list made on object
    
    '''list'''
    objects = []
    objects.append(object)
    print(objects[0].first)
    print("accessing A first list")    
    print(objects[0].second.first)
    print("accessing A second list")
    print(objects[0].second.second)
    
    '''
    #working with list inside methods of the objects
    print("accessing A second list .appended")
    object.second[1].second = 24214
    object.display()
    '''
    

    object.first = "B appended"
    object.second.first = "A first Appended"
    object.second.second = "A second Appended"
    print("Accessing appended objects")
    print(objects[0].first, objects[0].second.first, objects[0].second.second)

    ''' using for in - yeah'''

    objects.append(object)
    print("for list of item in the same object")
    for thelist in objects:
        thelist.display()

    ''' using for in - wiht a different object'''
    object = B()
    objects = []
    objects.append(object)
    object.first = "first appended in a different object"
    object.second.first = "second - first appended in a different object"
    object.second.second = "second - second appended in a different object"
    object.second.price = 45
    print("for list of item in a different object")
    count = 0
    for thelist in objects:
        count += 1
        print(count)
        thelist.display()

    ''' using for in - with  various different object'''

    objectA = B()
    objects = []
    objects.append(objectA)    
    objectA.first = "AA first appended in a different object"
    objectA.second.first = "AA second - first appended in a different object"
    objectA.second.second = "AA second - second appended in a different object"
    objectA.second.price = 55
    objectB = B()
    objects.append(objectB)
    objectB.first = "BB first appended in a different object"
    objectB.second.first = "BB second - first appended in a different object"
    objectB.second.second = "BB second - second appended in a different object"
    objectB.second.price = 66
    objectC = B()
    objects.append(objectC)    
    objectC.second.price = 67

    objectD = B()
    objects.append(objectD)    
    objectC.second.price = 52



    print("for list of item in a different object")
    count = 0
    for thelist in objects:
        count += 1
        print(count)
        thelist.display()
print("price")
print(objects[1].second.price)

print("sum elements in a list")
count_product = 0
suma = 0
for thelist in objects:
    new_product = objects[count_product].second.price
    print(new_product, "+ ")
    suma += new_product
    count_product += 1
print(suma)
    #suma = 0
    #suma += 