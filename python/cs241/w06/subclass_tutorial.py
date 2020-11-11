class Fish:
    def __init__(self, first_name="", last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")
    
...
class Trout(Fish):
    #def __init__(self, water = "freshwater"):
     #   self.water = water
        #super().__init__(self)
        pass
...

...
class Printing(Fish):
    def display(self):
        print("first name\n {}\nsecond name\n{}skelenton\n{}\neyelids{}".format(self.first_name,self.last_name,self.skeleton,self.eyelids))
    def listing(self):
        list=[self.first_name,self.last_name,self.skeleton,self.eyelids]
        print(list)
class Clownfish(Fish):

    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")
class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
    
class Coral:

    def community(self):
        print("Coral lives in a community.")


class Anemone:

    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


class CoralReef(Coral, Anemone):
    pass



terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

great = Printing("novo nome","why","who",True)
great.display()
great.listing()

casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()

sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)


terry = Trout()

# Initialize first name
terry.first_name = "Terry"

# Use parent __init__() through super()
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)

# Use child __init__() override
#print(terry.water)

# Use parent swim() method
terry.swim()


great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()