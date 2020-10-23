class A:
    def __init__(self):
        self.foo =  5

class B:
    def __init__(self):
        self.foo = 7
        self.bar = A()
    def display(self):
        print(self.foo, self.bar.foo)

if __name__ == "__main__":
    b_object = B()
    b_object.display()
    print(b_object.foo)
    print(b_object.bar.foo)