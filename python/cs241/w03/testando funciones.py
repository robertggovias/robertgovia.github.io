import math

class Point:
    def __init__(pedo, pX,pY):
        pedo.x = pX
        pedo.y = pY
    def gX(pedo):
        return pedo.x
    

    def gY(pedo):
        return pedo.y
    def distanceFromOrigim(pedo):
        return ((pedo.x ** 2)+(pedo.y**2))**0.5
    def __str__(pedo):
        return "x= "+ str(pedo.x)+"y= "+str(pedo.y)
        

def distance(p1, p2):
    xdiference = p2.gX() - p1.gX()
    ydiference = p2.gY() - p1.gY()

    distanteee = math.sqrt(xdiference**2 + ydiference**2)
    return distanteee



c = Point(10,10)
q = Point(5,5)
print(c.gX())
print(c.gY())
print(q.gX())
print(q.gY())
print(distance(c,q))
print(c)