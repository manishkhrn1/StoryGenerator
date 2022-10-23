"""
My Name is Manish Khurana
My student id is 991705696
"""

class Departures():                                  #We created a class called Departures
    def __init__(self):                               # We declared the constructor here and used the self parameter to initialise the values
        self.departingTime= "00:00"
        self.status= "status"
        self.destination="destination"
        self.airlineName="airlineName"                   #We declared the value , so that the constructor can pick up the value
        self.flightNo = 'flightNo'
        self.terminalNo = 'terminalNo'
        self.gateNo = 'gateNo'

firstFlight= Departures() 
departingTime= "15:00"
firstFlight.departingTime ="15:00"
status = "DELAYED"
destination = "DENVER - USA"
airlineName = "AIR CANADA"                       #here we initialized the values again as per the info
flightNo = "AC6436"
terminalNo = "T3"
gateNo = "R56"
                      #Here we are calling the class in this variable

print("                           Departures                         ")
print(firstFlight.departingTime, "    ", firstFlight.status  ,"    " ,firstFlight.destination , "   " , firstFlight.airlineName , "   " , firstFlight.flightNo , "   " , firstFlight.terminalNo , "   " , firstFlight.gateNo) 

"""
departingTime= " 2:00"                        
status = "ON TIME"
destination = "MONTREAL - QC"                                     
airlineName = "WESTJET"        
flightNo = "WS5621"
terminalNo = "T1"
gateNo = "E56"
"""
#The variables above have outdated values so we are gonna update the values

departingTime= " 6:00"                        
status = "DELAYED"
destination = "MONTREAL - QC"                   #This is the updated information of this departure                  
airlineName = "WESTJET"                         
flightNo = "WS5621"
terminalNo = "T1"
gateNo = "A45"

secondFlight= Departures()
print(secondFlight.departingTime, "    ", secondFlight.status  ,"    " ,secondFlight.destination , "   " , secondFlight.airlineName , "   " , secondFlight.flightNo , "   " , secondFlight.terminalNo , "   " , secondFlight.gateNo)