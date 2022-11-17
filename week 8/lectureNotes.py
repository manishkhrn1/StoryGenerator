class test():

    def __init__(self):
        self.varName1 = ""
        self.varNum1 = 0

    def changeName(self,newName):
        self.varName1 = newName
        anyName="PROG10004"

    def changeNumber(self,newNumber):
        self,varNum1=  newNumber

    def createNewNum(self,num1,num2):
        self.varNum1 = num1 + num2
        newVar = self.varNum1
        return newVar

    def createNewName(self,name1,name2):
        self.varName1= name1 + name2
        newStr = self.varName1
        return newStr
    
    #Acess the attributes(Actuator)
    def getVarName1(self):
        return self.varName1
    
    #mutate the value of the attribute of varName1 (Mutator)
    def setVarName1(self,newName):
        self.varName1=newName

test1 = test()
test2= test()

test1.varName1 = "PROG10004"
test.varNum1= 99

test1.changeName("Math10025")
print(test1.varName1)

test1.createNewName("Saaho " , "Chutiya")
print(test1.createNewName("Saaho " , "Chutiya"))

test2.varName1="Tele10025"
test1.varNum1 = 50

print(test2.getVarName1())

test2.setVarName1("Prog10004")
print(test2.getVarName1())