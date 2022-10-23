import random

def askForSensor(number,totalSensors):
    number=1
    numberOfSensor=str(input("Enter the number of sensors deployed across Sheridan Campus: "))
    while not numberOfSensor.isdigit() :
        numberOfSensor=str(input("Enter the number of sensors deployed across Sheridan Campus: "))   # we declared a variable for number of sensors we wanna input
    totalSensors= int(numberOfSensor)
    #positionOfSensor(x,y,number,totalSensors,average)
    
    return totalSensors,number

def positionOfSensor(x,y,number,totalSensors , average): 
    for number in range (1,totalSensors+1):
        x=random.uniform(0.00,100.00)
        y=random.uniform(0.00,100.00)
        x=round(x,2)
        y=round(y,2)
        sensorPosition=[x,y]
        print("This is for Sensor" ,number ,"at position ",sensorPosition, " :")
        days = int(input("Enter the number of days for the readings: "))
        number+=1
        readingsOfCO(average,days,number,totalSensors)
        return number
    

def averageOfReadings(days,number,average,totalSensors):
    
    roundedAverage=sum(average)/days
    print("Rounded Average Readings", (round(roundedAverage,2)), "PPM" )
    #if(days>1):
    #    number+=1
    #    positionOfSensor(x,y,number,totalSensors,average)
        
    return roundedAverage,number,totalSensors

def readingsOfCO(average,days,number,totalSensors):
    for i in range(1,days+1):
        print("Enter the CO2 for Day", i ," : " )
        CO=int(input())                         # We declared a variable 'CO' , which is carbon dioxide for days
        i+=1
        average.append(CO)
        # average.append(CO)
    averageOfReadings(days,number,average,totalSensors)
            #sumofCO = sumOfCO + CO

x=int
y=int
average=[]
number = 1
totalSensors=2
askForSensor(number,totalSensors)

while True:
    #askForSensor(totalSensors, number)
    #print(totalSensors)
    while number != totalSensors:
        positionOfSensor(x,y,number,totalSensors , average)
        number+=1
        break
        
        