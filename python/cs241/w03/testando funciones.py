class Point:
    def __init__(self, pX,pY):
        self.x = pY
        self.y = pY
    def gX(self):
        return self.x
    
    def gY(self):
        return self.y
        
p = Point(4,5)
print(p.gX())
print(p.gY())

p2 = Point(1,2)
print(p2.gX())
print(p2.gY())