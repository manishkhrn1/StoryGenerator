'''
list1=['B',10,'C',12]
list2=['A',14,'D',34]
tList1=tuple(list1)
tList2=tuple(list2)
dict1=dict(zip(list1,list2))
#dict1[tList1]=tList2
print(dict1)
dict2={4:32,5:65    }
dict2.update(dict1)
print(dict2)
dict2={}
print(dict2)
'''
'''
dict1 = {'A': {'B': 12, 'C': 13}, 'B': {'A': 12, 'C': 14}}
lol=dict1.values()
print(lol)
print(dict1.keys())
rofl=dict1.pop('A')
print(rofl)
print(rofl.get('B'))
print(rofl.values())
lmao=list((rofl.values()))
print('lmao : ',lmao)
'''
dict1 = {'A': {'B': 12, 'C': 13}, 'B': {'A': 12, 'C': 14}}
print(dict1.())
"""
from wirelessNetwork import *       #Importing another class to use for executing

class Application:              #This class is the main class that will make  the sensors
    def __init__(self):
        self._listSensors= []
        self._neighbour = ''
        self._listNeighbour=[]
        self._distance=0
        self._listDistance=[]
        self._dict={}
        
    
    def createSensors(self):        #This class will create the sensor
        sensor = str(input("Enter the number of sensors: "))
        while not sensor.isnumeric():               #If the input is not numeric then it will keep on asking about the number of sensor
            print("This is an invalid entry for the number of sensors")
            sensor = str(input("Enter the number of sensors: "))
        sensor = int(sensor)                #To change the type from String to Number
        for i in range (sensor):               #It will run a loop depending on the number of sensors
            print("_*_*_*_*_*_*_*_*_*_*_*_*_")
            self._sensorId = str(input("Enter the sensor ID : "))   #It will store the sensor ID 
            while not self._sensorId.isalpha():                     #It will keep on asking the sensor ID until its  fully alphabetical 
                print("THis is an invalid entry for sensor ID!")
                self._sensorId = str(input("Enter the sensor ID : "))
            self._listSensors.append(self._sensorId)                #It will add it to the list of sensors
            neighbour = str(input("Enter the number of neighbours : ")) 
            while not neighbour.isnumeric():
                print("Invalid Entry")
                neighbour = str(input("Enter the number of neighbours : "))
            neighbour = int(neighbour)
            for j in range (neighbour): 
                self._neighbour = str(input("Enter the neighbor of Sensor " + self._sensorId + ": " ))
                while not self._neighbour.isalpha():
                    print("Invalid Entry")
                    self._neighbour = str(input("Enter the neighbor of Sensor " + self._sensorId +":" ))
                self._listNeighbour.append(self._neighbour)
                self._distance = str(input("Enter the distance to " + self._sensorId + ": " ))
                while not self._distance.isdigit():
                    print("Please enter a nummerical value")
                    self._distance = str(input("Enter the distance to " + self._sensorId , ":" ))
                self._distance=int(self._distance)
                self._listDistance.append(self._distance)
                oxygen = str(input("Enter the Oxygen level in %: " ))
                while not oxygen.isdigit():
                    print("Invalid Entry")
                    oxygen = str(input("Enter the Oxygen level in %: " ))
                oxygen = int(oxygen)    
                value = False
                while value!=True:
                    try:
                        temperature =float(input("Enter the temperature measurement : "))
                        value = True
                    except:
                        print("Please enter a valid number!")
            self.convertToDictionary()
            self._listDistance.clear()
            self._listNeighbour.clear()            

    def convertToDictionary(self):
        dict1={}
        dict2 ={}
        #dict2[self._neighbour]= self._distance
        #dict1[self._neighbour]=self._distance
        dict1[self._sensorId]={}
        lol=self._listNeighbour
        rofl=self._listDistance
        dict2=dict(zip(lol,rofl))
      #  dict1[self._sensorId][self._neighbour]=self._listDistance
        dict1[self._sensorId]=dict2
        self._dict=self._dict|(dict1)
        #dict5=dict4|dict1
        print("this is dict 2" ,dict2)
        print(dict1)
        print("This is dict4" ,self._dict)
        print(lol)
        print(rofl)


    def findPath(self):
        longestPath = self._listSensors[0]
        for i in self._listSensors:
            if i > longestPath:
                longestPath = i
                return longestPath 





  #          source = str(input("Enter the source sensor :" ))
   #         destination = str(input("Enter the destination sensor : "))
            

obj1 = Application()
obj2 = WirelessNetwork()
obj2.greetMessage()
obj1.createSensors()

"""