import random

def askForSensor():
    numberOfSensor=str(input("Enter the number of sensors deployed across Sheridan Campus: "))
    while not numberOfSensor.isdigit() :
        numberOfSensor=str(input("Enter the number of sensors deployed across Sheridan Campus: "))   # we declared a variable for number of sensors we wanna input   
    positionOfSensor(x,y,number,numberOfSensor)
    return numberOfSensor

def positionOfSensor(x,y,number,numberOfSensor): 
   while number != numberOfSensor :
    for number in range (1,numberOfSensor+1):
        
        x=round(x,2)
        y=round(y,2)
        sensorPosition=[x,y]
        print("This is for Sensor" ,number ,"at position ",sensorPosition, " :")
        days = int(input("Enter the number of days for the readings: "))
        number+=1
        readingsOfCO(average,days)
        return number
    

    


def averageOfReadings(days,number):
    
    roundedAverage=sum(average)/days
    print("Rounded Average Readings", (round(roundedAverage,2)), "PPM" )
    #if(days>1):
    #    number+=1
    #    positionOfSensor(x,y,number)
    return roundedAverage

def readingsOfCO(average,days):
    for i in range(1,days+1):
        print("Enter the CO2 for Day", i ," : " )
        CO=int(input())                         # We declared a variable 'CO' , which is carbon dioxide for days
        i+=1
        average.append(CO)
        # average.append(CO)
    averageOfReadings(days,number)
            #sumofCO = sumOfCO + CO

        

sumOfCO = 0    
x=random.uniform(0.00,100.00)
y = random.uniform(0.00,100.00)
#numberOfSensor=1
number =0
average=[]
CO=0
i=0
running = True
roundedAverage= 0
sensorPosition=[0,0]
ask=''
#days=0
askForSensor()
#print(numberOfSensor)
#while number!=numberOfSensor:
 #   positionOfSensor(x,y,number)
  #  number+=1

#days = int(input("Enter the number of days for the readings: "))
#readingsOfCO(average)


'''while running!=False:
    
    while(number!=numberOfSensor+1):

        positionOfSensor(x,y)

        print("This is for sensor",number,"at position", (x,y))
        days=int(input("Enter the number of days : "))
        number +=1 
        readingsOfCO()
        average.append(CO)
        roundedAverage= sum(average)/days
        print(roundedAverage)

   
    while ask!=False:
        cont=str(input("Do you wanna Proceed : (Y)es or (N)o :" ))
        if cont.lower() in ["y", "yes"]:
            running = True
            ask=False
        elif cont.lower() in ['n' ,"no"]:
            print("Exiting the program..........")
            running = False 
            ask=False
        else:
            print("Invalid response")
            ask = True'''