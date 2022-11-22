class Shape:
    """This class creates different shapes"""
    cat = 'Geometry'

    def __init__(self,type):
        self._type = type
        self.num = 1

    def show(self):
        Shape.cat = 'New Geometry'
        print("This is a category : " , Shape.cat)
        self.cat = "None"
        print('Shape is ', self.cat)
        print("Type" , self._type)

    @staticmethod
    def info(msg):
        print(msg)
        print("this class is used for representing shapes")

Shape.cat= 'New Geometry'

firstObj = Shape("triangle")
firstObj.cat='triangle'
firstObj.show()
print(firstObj.cat)

secondObj = Shape("Circle")
print(secondObj.cat)