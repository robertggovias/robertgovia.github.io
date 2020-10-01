class Student:
    init_first=""
    init_last=""
    init_id=0

    def __init__(self, init_first, init_last, init_id):
        self.first = init_first
        self.last = init_last
        self.id = init_id
    
    def gf(self):
        return self.first
    
    def lf(self):
        return self.last
    
    def i_f(self):
        return self.id
        
p = Student(4,7,7)
print(p.gf())
print(p.lf())
print(p.i_f())