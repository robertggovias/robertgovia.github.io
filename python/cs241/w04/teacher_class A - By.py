class A:
    def __init__(self):
        self.first =  1
        self.second =  2

class B:
    def __init__(self):
        self.first = "B"
        self.second = A()

        # create a list as object
        '''
        self.second = [A(),A()]
        '''
    #nomal inheritance
    def display(self):
        print(self.first, self.second.first, self.second.second)
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

    ''' using for in - wiht  aidfferent object'''
    object = B()
    objects = []
    objects.append(object)
    object.first = 32
    object.first = 33
    object.first = "first appended in a different object"
    object.second.first = "second - first appended in a different object"
    object.second.second = "second - second appended in a different object"


    print("for list of item in a different object")
    count = 0
    for thelist in objects:
        count += 1
        print(count)
        thelist.display()




    