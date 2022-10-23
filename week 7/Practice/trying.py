import random

def askForSensor(number,totalSensors):
    number=1
    print()
    print("***********************************************************************************")
    print()
    numberOfSensor=str(input("Enter the number of sensors deployed across Sheridan Campus: "))
    while not numberOfSensor.isdigit():
        print()
        print("please enter a numerical value greater than 0")
        print()
        print()
        numberOfSensor=str(input("Enter the number of sensors deployed across Sheridan Campus: "))   # we declared a variable for number of sensors we wanna input
    totalSensors= int(numberOfSensor)
    positionOfSensor(x,y,totalSensors,average)

def positionOfSensor(x,y,totalSensors,average): 
    for number in range (1,totalSensors+1):
        x=random.uniform(0.00,100.00)
        y=random.uniform(0.00,100.00)
        x=round(x,2)
        y=round(y,2)
        sensorPosition=[x,y]
        print()
        print("This is for Sensor" ,number ,"at position ",(sensorPosition[0],sensorPosition[1]), " :")
        numberOfDays = str(input("Enter the number of days for the readings: "))
        days=int(numberOfDays)        
        while numberOfDays.isdigit()==False :
            print()
            print("Please enter a numerical value greater than 0")
            numberOfDays = str(input("Enter the number of days for the readings: "))
        number+=1
        #days=int(numberOfDays)
        readingsOfCO(average,days,number,totalSensors)
        #return number



def averageOfReadings(days,number,average,totalSensors):
    
    roundedAverage=sum(average)/days
    print()
    print("Rounded Average Readings", (round(roundedAverage,2)), "PPM" )
    average.clear()
    #if(days>1):
    #    number+=1
    #    positionOfSensor(x,y,number,totalSensors,average)
        
    return roundedAverage,number,totalSensors ,average

def readingsOfCO(average,days,number,totalSensors):
    for i in range(1,days+1):
        print()
        whatDay=str(i)
        #print("Enter the CO2 for Day", i ," : " )
        CO=int(input("Enter the CO2 for the Day " + whatDay +" :"))                         # We declared a variable 'CO' , which is carbon dioxide for days
        i+=1
        average.append(CO)
        # average.append(CO)
    averageOfReadings(days,number,average,totalSensors)
            #sumofCO = sumOfCO + CO

x=int
y=int
average=[]
number = 0
condition=0
totalSensors=0
running=True
ask = True
while running!=False:
    askForSensor(number,totalSensors)
    while ask !=False:
        print()
        cont=str(input("Do you wanna Proceed : (Y)es or (N)o :" ))
        if cont.lower() in ["y", "yes"]:
            askForSensor(number,totalSensors)

        elif cont.lower() in ['n' ,"no"]:
            print("Exiting the program..........")
            running=False 
            ask=False
        else:
            print("Invalid response")
            
'''
while True:
    #askForSensor(totalSensors, number)
    #print(totalSensors)
    while number != totalSensors:
        positionOfSensor(x,y,number,totalSensors , average)
        number+=1
        break
   '''   
        