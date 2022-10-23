import random

def askForSensor(number,totalSensors):                                  #we created a function ,which asks us about the sensors present acroos the campus
    number=1
    print()
    print("***********************************************************************************")
    print()
    numberOfSensor=str(input("Enter the number of sensors deployed across Sheridan Campus: "))          #here we ask the user to input the number of sensor
    while numberOfSensor.isdigit()==False or numberOfSensor.isdigit()<1:                                #here we added a loop so that it will keep on asking us number of sensors until we give it an int value
        print()
        print("please enter a numerical value greater than 0")
        print()
        print()
        numberOfSensor=str(input("Enter the number of sensors deployed across Sheridan Campus: "))   # we declared a variable for number of sensors we wanna input
    totalSensors= int(numberOfSensor)                              #We  converted the string to the integer value

    positionOfSensor(x,y,number,totalSensors,average)               #We called up another function with that

def positionOfSensor(x,y,number,totalSensors , average):            #we declared another function here with the parameters from the previous function and global variables ,so that it can get the value of the variables 
    for number in range (1,totalSensors+1):
        x=random.uniform(0.00,100.00)
        y=random.uniform(0.00,100.00)                               #We declared here a variables to generate up a random number
        x=round(x,2)
        y=round(y,2)
        sensorPosition=[x,y]                                        #We created a list for sensorPosition
        print()
        print("This is for Sensor" ,number ,"at position ",(sensorPosition[0],sensorPosition[1]), " :") 
        print()
        numberOfDays = str(input("Enter the number of days for the readings: "))       #it will ask us how many number of days we want
        while  numberOfDays.isdigit()==False:                                                #It will not let user enter a character
            print()
            print("Please enter a numerical value greater than 0")
            numberOfDays= str(input("Enter the number of days for the readings: "))
        number+=1
        days=int(numberOfDays)                                                            #we changed the type because we need to divide an integer, which we can't divide by string
        readingsOfCO(average,days,number,totalSensors)                                         #We called another function




def averageOfReadings(days,number,average,totalSensors):                    #This function will give us average of the values of C02 
    
    roundedAverage=sum(average)/days                                   
    print()
    print("Rounded Average Readings", (round(roundedAverage,2)), "PPM" )            #This will round the decimal upto 2 decimal places
    average.clear()                                                                         #this will clear the average list , so that it won't keep the values

        
    return roundedAverage,number,totalSensors ,average

def readingsOfCO(average,days,number,totalSensors):                             #We declared another function
    for i in range(1,days+1):                                                     #we started a loop for the number of days , so that the program ask user for the desired input
        print()
        whatDay=str(i)
        #print("Enter the CO2 for Day", i ," : " )
        CO=int(input("Enter the CO2 for Day " + whatDay +  " : "))                         # We declared a variable 'CO' , which is carbon dioxide for days
        i+=1
        average.append(CO)                                                          #It will add up the average value
    averageOfReadings(days,number,average,totalSensors)                                 #We called up the previous function with this
        

x=int
y=int
average=[]
number = 0                                                          #We declared some function to be global , which can be used in every function
totalSensors=0
running=True
ask = True
while running!=False:                                               #We started a loop ,so that it will keep on running until user inputs n or no
    askForSensor(number,totalSensors)
    while ask !=False:                                                  #Here we started the loop so that program asks users until they put correct entry
        print()
        cont=str(input("Do you wanna Proceed : (Y)es or (N)o :" ))
        if cont.lower() in ["y", "yes"]:
            askForSensor(number,totalSensors)

        elif cont.lower() in ['n' ,"no"]:
            print("Exiting the program..........")
            running=False 
            ask=False
        else:
            print("Incorrect Entry! Please Try Again")
    