from co2_sensors import Co2Sensors #We imported co2sensors, because this class is dependant on Co2Sensor

#This class will make the Buildings
class Building():
    def __init__(self):
        self._building= ""
        self._noOfSensor = ""
        self._listOfSensor = []

#This will create the Sensors and access it from Co2 Class
    def createSensor(self):
        self._noOfSensor=(input('Enter the number of sensor deployed across Sheridan Campus : '))   
        while not (self._noOfSensor.isnumeric()):
           print("Invalid input, Please input again")  
           self._noOfSensor=(input('Enter the number of sensor deployed across Sheridan Campus : ')) 
        self._noOfSensor=int(self._noOfSensor)     
        for i in range (self._noOfSensor):
            print("Sensor",i+1)
            self.co2Obj = Co2Sensors()
            self.co2Obj.sensorPos()
            self.co2Obj.sensorReadings()
            self._listOfSensor.append(self.co2Obj)
            
#This is an accessor to get Building Name
    def getBuildName(self):
        return self._building
#This is an mutator to set Building Name
    def setBuildName(self,name):
        self._building = name

#This is an accessor to get Number of sensors    
    def getNumSensor(self):
        return self._noOfSensor

#This is an mutator to set number of sensors    
    def setNumSensor(self,numSensor):
        self._noOfSensor = numSensor

#This is an accessor to get list of sensors
    def getList(self):
        return self._listOfSensor

#This is an mutator to set list of sensors
    def setList(self,newList):
        self._listOfSensor= newList
            
#This is method which will print all the data 
    def printSenInfo(self):
        print("************************************")
        print("This is for building :", self._building)
        print("************************************")
        
        for i in range (len(self._listOfSensor)):
            sensor=self._listOfSensor[i]
            print("Sensor" ,i+1)
            print("X :" , (sensor.getX()))
            print("Y :" , (sensor.getY()))
            for j in range (len(sensor._co2Levels)):
                print("Day {0} :".format(j+1),sensor._co2Levels[j])
            print("Average Reading :" , sensor.getAvg())
            print("***************")
            print("***************")

