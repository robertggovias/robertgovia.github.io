class ExampleClass:
    '''This class illustrates using protect4ed and private variables in Python'''
    def __init__(self):
        self.a = 'a'
        self._b ='b'
        self.__c = 'c'
        self.__d = 'd'

        self.__b_read_accesses = 0
        self.__b_write_accesses = 0
        self.__c_read_accesses = 0
        self.__c_write_accesses = 0
        self.__d_read_accesses = 0
        self.__d_write_accesses = 0

    def get_b(self):
        self.__b_read_accesses += 1
        return "{} has been accessed {} times".format(self._b, self.__b_write_accesses)

    def set_b(self, val):
        self.__b_write_accesses += 1
        print("B has been written {} times".format(self.__b_write_accesses))
        self._b = str(val)

    @property
    def c(self):
        self.__c_read_accesses += 1
        return "{} has been accessed {} times".format(self.__c, self.__c_write_accesses)   

    @c.setter
    def c(self, val): 
        self.__c_write_accesses += 1
        print("c has been written {} times".format(self.__c_write_accesses))
        self.__c = str(val)

    def __get_d(self):
        self.__d_read_accesses += 1
        return "{} has been accessed {} times".format(self.__d, self.__d_write_accesses)

    def __set_d(self, val):
        self.__d_write_accesses += 1
        print("D has been written {} times".format(self.__d_write_accesses))
        self._d  = str(val)
    
    d = property(__get_d, __set_d)

class DerivedClass(ExampleClass):
    '''This demonstrates how the derived clas handles private variables'''
    def __init__(self):
        super().__init__()
        self.__c = 'Moo'
        self.__d = 'Quack'
    
    def display(self):
        print(self.a)
        print(self._b)
        print(self.__c)
        print(self.__d)
        self.c = 'Baa'
        self.d = 'Woof'
        print(self.c)
        print(self.d)
    
if __name__ == "__main__":    
    obj = DerivedClass()
    obj.display()
    


