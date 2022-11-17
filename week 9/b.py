from a import A

#This is a child Class
class B(A):
    def __init__(self):
        super().__init__()
        self.classBvar = "Class B"
        self.insideB = "Inside B Class"
        #self.insideB= self.insideVarName1
        print("This is B's __init__()")

print("--------------A-----------")
varA= A()
#print(varA.insideVarNameInt)
#print(varA.insideVarName1)

print("--------------Class B---------")
varB = B()
print(varB.classBvar)
print(varB.insideB)
print(varB.insideVarName1)
varB.insideVarNameInt= 100
varB.insideVarName1 = "Class A"
print(varB.insideVarNameInt)
print(varB.insideVarName1)