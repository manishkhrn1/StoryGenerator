'''
This is a code for circle
Written by Manish
'''

PI_Circle = 3.14

radius= 0.0
areaCircle = 0.0
perimeterCircle = 0.0

radiusStr = input("Enter the radius of the Circle: ")
#radius = int(radiusStr)
radius = float(radiusStr)

areaCircle= PI_Circle *(radius*radius)
#areaCircle= PI_Circle *(radius**2)
#areaCircle= PI_Circle *(pow(radius,2))

perimeterCircle = 2 * PI_Circle * radius

print("The area of the Circle is : " ,areaCircle)
print("The perimeter is : ", perimeterCircle)