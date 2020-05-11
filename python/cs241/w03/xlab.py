import math
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(s,ix,iy):
        """ Create a new point at the origin """
        s.x = ix
        s.y = iy
    def getX(s):
        return s.x
    def getY(s):
        return s.y
    def distanceFromOrigin(s):
        return((s.x ** 2) + (s.y ** 2)) ** 0.5
    
    
def distance(point1, point2):
    xdiff = point2.x - point1.x
    ydiff = point2.y - point1.y

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist


p = Point(10,10)         # Instantiate an object of type Point
q = Point(9,4)         # and make a second point

print(p.x,p.y)
print(p.getX())
print(p.getY())
print(p.distanceFromOrigin())
print(distance(p,q))