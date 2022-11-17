class Cereal():
    def __init__(self,name,brand,fiber):
        self._name=name
        self._brand=brand
        self._fiber= fiber
        
    def getName(self):
        return self._name
    def getBrand(self):
        return self._brand
    def getFiber(self):
        return self._fiber
    def instance(self):
        return (self._name , "cereal is produced by " , self._brand , " and fiber is " ,self._fiber,"grams of fiber in every serving!")

    
c1= Cereal("Corn Flakes","Kellogg's" , 2)
c2=Cereal("Honey nut Cheerios","General Mills",3) 
print(c1.instance())
print(c2)
    