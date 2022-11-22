#This is the parent Class of Co2Sensors
class IotSensor():                                              
    def __init__(self,posX,posY,noDays,avgRead):
        self._posX=posX
        self._posY=posY
        self._noDays=noDays
        self._avgRead=avgRead


    def sensorReadings():
        pass
    def SensorPos():
        pass
    def computeAvg():
        pass