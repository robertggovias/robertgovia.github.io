import math

class Point:
    def __init__(self, pX,pY):
        self.x = pX
        self.y = pY
    def gX(self):
        return self.x
    
    def gY(self):
        return self.y
    def distanceFromOrigim(self):
        return ((self.x ** 2)+(self.y**2))**0.5

def distance(p1, p2):
    xdiference = p2.gX() - p1.gX()
    ydiference = p2.gY() - p1.gY()

    distanteee = math.sqrt(xdiference**2 + ydiference**2)
    return distanteee
        
p = Point(4,5)
q = Point(7,9)
print(p.gX())
print(p.gY())

print(distance(p,q))