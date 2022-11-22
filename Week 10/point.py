from math import sqrt
class Point:
    def __init__(self,x,y):
        self._x=x
        self._y=y

    def getX(self):
        return self._x

    def getY(self):
        return self._y    
    def add(self,another):
        print("x:" ,self._x + another._x )
        print("y:",self._y + another._y) 

    def subtract(self,another):
        print("x:" , self._x - another._x)
        print("y:" , self._y-another._y)
    def compare(self,another):
        p1=sqrt(((self._x)**2) - ((self._y)**2))
        p2=sqrt((another._x)**2 - (another._y)**2)
        if p1> p2:
            print ("Point 1 is greater than point 2")
        else :
            print("point 2 is greater than point 1")



point1 = Point(2,4)
point2 = Point(3,5)

#print(point1 + point2)
Point.add(point1,point2)
Point.subtract(point1,point2)
Point.compare(point1,point2)

