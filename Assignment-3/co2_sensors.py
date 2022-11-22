from IoTSensors import IotSensor    #We imported the IotSensor class ,as it is the Parent class
import random  #To import a random number

class Co2Sensors(IotSensor):    
    def __init__(self):
        self._co2Levels= []

#This Method will make a random sensor
    def sensorPos(self):
        self._posX=random.uniform(0.00,100.00)
        self._posY=random.uniform(0.00,100.00)
        self._posX=round(self._posX,1)
        self._posY=round(self._posY,1)
       
        
#This is an accessor to get value of x
    def getX(self):
        return self._posX
    
#This is a mutator to get vzlue of y
    def getY(self):
        return self._posY



#This method will generate the sensors required.
    def sensorReadings(self):
        self._noDays = (input("Enter the number of days for the sensor(s) to collect CO2 levels : "))
        while not (self._noDays.isnumeric()):
            print()
            print("Invalid Input,please try again.")
            self._noDays = (input("Enter the number of days for the sensor(s) to collect CO2 levels : "))
        self._noDays=int(self._noDays)        
        for i in range(self._noDays):
            self.co2Readings = (input("Enter the CO2 Reading (PPM) for Day  {0} : ".format(i+1) ))
            while not (self.co2Readings.isnumeric()):
                print("Please enter a valid input!")
                self.co2Readings = (input("Enter the CO2 Reading (PPM) for Day  {0} :".format(i+1)))
            self.co2Readings=int(self.co2Readings)
            self._co2Levels.append(self.co2Readings)
        print()
        self._avgRead=self.computeAvg() 

            
       
#This is an accessor to get coLevels
    def getCoLevel(self):
        return self._co2Levels

#This is a mutator to set coLevels
    def setCoLevel(self,newCo):
        self._co2Levels=newCo
#This is a mutator to set Avg
    def setAvg(self,avgRead):
        self._avgRead= avgRead

#This is an accessor to get coLevels
    def getAvg(self):
        return self._avgRead


    def computeAvg(self):
        counter=0
        for i in range (len(self._co2Levels)):
            counter += self._co2Levels[i]
        return counter/len(self._co2Levels)