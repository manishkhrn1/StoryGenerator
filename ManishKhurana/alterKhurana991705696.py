import random                       #We imported this to add a random no.

running = True                      # We declared a variable to use in while loops
number=1                            # We declared a variable number  to determine how many times the loop will run   
#days=0                               
#CO=0                                
numberOfSensor=0                    

#sensor=[x,y]
#cont=''
ask=True
while (running != False):
    average=[]
    print()
    print("******************************************************************************")
    print()
    numberOfSensor=int(input("Enter the number of sensors deployed across Sheridan Campus: "))   # we declared a variable for number of sensors we wanna input
    print()
    while number!=(numberOfSensor+1):
            x=  random.uniform(0.00,100.00)
            y= random.uniform(0.00,100.00)
            x=round(x,2)
            y=round(y,2)
            sensor=[x,y]
            print("This is for Sensor" ,number ,"at position ",sensor)
            print("")
            days = int(input("Enter the number of days for the readings: "))  # We declared variable days to initialize the number of days, the user want to add data for
            print()
            number+=1
        
            for i in range (1,days+1):
                print("Enter the CO2 for Day", i ," : " )
                CO=int(input())                         # We declared a variable 'CO' , which is carbon dioxide for days
                average.append(CO)
                i+=1
                roundedAverage= (sum(average))/days     #We declared this variable to round off the number 
            print("Rounded Average Readings", (round(roundedAverage,2)), "PPM" )
            print("")
            average.clear()
        
    number=1
    proceed= "y" or "yes" or "Y" or "Yes" or "YES"
    end = "n" or "no" or "NO" or "No" or "N"
    while ask!=False:
        cont=str(input("Do you want to continue: (Y)es or (N)o: "))
        print()
        if cont == proceed:
            running=True
            ask=False
        elif cont == end:
            print("Exiting the Program............")
            running = False
            ask=False
        else:
            print("Please enter a valid response")
            ask=True







    


