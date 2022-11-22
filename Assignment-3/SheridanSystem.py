#We are importing Building class to access the information to create sensor and print the data
from building import Building 

class SheridanSystem():
    def __init__(self):
        self.numOfBuildings = 0

#This method will run and access the Building class to create sensor and print information required
    def run(self):
        self.numOfBuildings=(input("Enter the number of Buildings : "))
        while not (self.numOfBuildings.isnumeric()):
            print("Invalid input! Please Enter Again")
            self.numOfBuildings=(input("Enter the number of Buildings : "))
        self.numOfBuildings=int(self.numOfBuildings)
        for i in range (self.numOfBuildings):
            buildName = Building()                                  #This is the object of Building
            buildName._building=input("Enter the name of the Building {0}:".format(i+1))
            while not (buildName._building.isalpha()):
                print("Invalid Input, Please Enter Again!")
                buildName._building=input("Enter the name of the Building {0}:".format(i+1))
            buildName.createSensor()                    #This will Access the Create Sensor method of Building class
            buildName.printSenInfo()                #This will access the print method of Building class



 