import math

class Points:
    def __init__(self,newXCoord,newYCoord):
        self.xCoord = newXCoord
        self.yCoord = newYCoord

    def getXCoord(self):
        return self.xCoord

    def setXCoord(self, newXCoord):
        self.yCoord= newXCoord        
    
    def getYCoord(self):
        return self.yCoord

    def setYCoord(self, newYCoord):
        self.yCoord= newYCoord

    def distance(self,point2):    
        diffX = self.getXCoord() - point2.getXCoord()
        diffY = self.getYCoord() - point2.getYCoord()

        distance = math.sqrt((diffX**2) - (diffY**2))
        return distance

def distance(point1,point2):    
    diffX = point1.getXCoord() - point2.getXCoord()
    diffY = point1.getYCoord() - point2.getYCoord()

    distance = math.sqrt((diffX**2) - (diffY**2))
    return distance

point1 = Points(10,7)
point2 = Points(5,6)

actualDis= distance(point1 , point2)

print(round(actualDis,2))

actualDis= point1.distance(point2)
print(round(actualDis,2))