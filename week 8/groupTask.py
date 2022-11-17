from math import *



class Points:
    def __init__(self,x,y):
        self.xcoord=x
        self.ycoord=y
    
    def distanceFromOrigin(self):
        length = (self.xcoord**2) + (self.ycoord**2)
        distance= sqrt(length)
        print ("The distance from the origin is : " , distance)

    

x= float(input("Please enter the value of x : "))
y=float(input("Please enter the value of y : "))
origin=Points(x,y)
origin.distanceFromOrigin()

