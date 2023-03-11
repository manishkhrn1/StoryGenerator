from wirelessNetwork import *       #Importing another class to use for executing

class Application(WirelessNetwork):              #This class is the main class that will make  the sensors
    def __init__(self):
        self._sensorId=WirelessNetwork()
        self._oxygenLevel= WirelessNetwork()
        self._temperature=WirelessNetwork()
        self._listSensors= []
        self._listNeighbour=[]
        self._listDistance=[]
        self._dict={}
        self._dict1={}
        self._path=[]


        
    
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
                neighbourSen = str(input("Enter the neighbor of Sensor " + self._sensorId + ": " ))
                while not neighbourSen.isalpha():
                    print("Invalid Entry")
                    neighbourSen = str(input("Enter the neighbor of Sensor " + self._sensorId +":" ))
                self._listNeighbour.append(neighbourSen)
                distance = str(input("Enter the distance to " + self._sensorId + ": " ))
                while not distance.isdigit():
                    print("Please enter a nummerical value")
                    distance = str(input("Enter the distance to " + self._sensorId , ":" ))
                distance=int(distance)
                self._listDistance.append(distance)
            self._oxygenLevel = str(input("Enter the Oxygen level in %: " ))
            while not self._oxygenLevel.isdigit():
                print("Invalid Entry")
                self._oxygenLevel = str(input("Enter the Oxygen level in %: " ))
            self._oxygenLevel = int(self._oxygenLevel)    
            value = False
            while value!=True:
                try:
                    self._temperature =float(input("Enter the temperature measurement : "))
                    value = True
                except:
                    print("Please enter a valid number!")

            #self._list1=list(self._dict.items())
            #self._list2.append(self._list1)
             
            self.convertToDictionary()
            self._listDistance.clear()
            self._listNeighbour.clear()
        self._source=str(input("Enter the source sensor : "))
        while not self._source.isalpha():
            print("Invalid Entry")
            self._source=str(input("Enter the source sensor : "))
        self._destination=str(input("Enter the destination sensor : "))
        while not self._destination.isalpha():
            print("Invalid Entry")
            self._destination=str(input("Enter the source sensor : "))
        self.findPath()
            
           
    def convertToDictionary(self):
        self._dict[self._sensorId]={}
        self._dict1= dict(zip(self._listNeighbour,self._listDistance))
        self._dict[self._sensorId]=self._dict1
        #print("This is dictionary" ,self._dict)  #To check the dictinonary

    def findPath(self):
        #source= str(input("Enter the source sensor : "))
        #destination= str(input("Enter the destination sensor :"))
        sensors = list(self._dict.keys())                    #To seprate the sensors

        if self._source==self._destination:
            self._path.append(self._source)
            return ('Path  = ' ,self._path)

        if self._source in sensors:
            
            self._path.append(self._source)
            sensors=self._dict.pop(self._source)
            keys=list(sensors.keys())
            values=list(sensors.values())
            longest=max(sensors.values())
            self._source = keys[values.index(longest)]
            return self._source

        else:
            self.findPath()


'''
    def findPath(self):
        self._source= str(input("Enter the source sensor : "))
        self._destination= str(input("Enter the destination sensor :"))
        sensors = list(self._dict.keys())                    #To seprate the sensors
        if self._source in sensors:
            self._path.append(self._source)
            sensors=self._dict.pop(self._source)
            keys=list(sensors.keys())
            values=list(sensors.values())
            longest=max(sensors.values())
            self._source = keys[values.index(longest)]
        
        else:
            self.findPath(self._source,self._destination)
            if self._source == self._destination:
                print(self._path)
'''


"""        longestPath = self._listSensors[0]
        for i in self._listSensors:
            if i > longestPath:
                longestPath = i
                return longestPath """


"""
I need source sensor
also destination 
final dictionary

"""


  #          source = str(input("Enter the source sensor :" ))
   #         destination = str(input("Enter the destination sensor : "))
            

obj1 = Application()
obj2 = WirelessNetwork()
obj2.greetMessage()
obj1.createSensors()