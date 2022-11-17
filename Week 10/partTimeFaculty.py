import employee
class PartTimeFacculty(employee):
    def __init__(self,):
        self._hourlywage=0.0
        self._biWeeklyHours = 0.0
        self._pay=0.0

    def setHourlyWage(self,newHourlyWage):
        self._hourlywage = newHourlyWage

    def setBiWeekly(self,newBiWeekly):
        self._biWeeklyHours= newBiWeekly

    def setPay(self,newPay):
        self._pay= newPay
    def getHourlyWage(self):
        return self._hourlywage

    def getBiWeekly(self):
        return self._biWeeklyHours

    def getPay(self):
        return self._pay

    def calculatePay(self):
        self._pay=self._hourlywage * self._biWeeklyHours
        return self._pay

    def toString(self):
        return (super().toString()+  "    " + "Hourly Wage :  " + str(self._hourlyWage) + "    " 

