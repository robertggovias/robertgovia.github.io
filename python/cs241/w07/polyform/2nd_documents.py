class Animals:
    def __init__(self,name):
        self.name=name
    
    def show(self):
        print("This funny {} need a bath".format(self.name))

class Rocks(Animals):
    pass

cat = Animals("cat")
rock = Rocks("diamond")

cat.show()
rock.show()