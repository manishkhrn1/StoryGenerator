import person

class Employee(person):
    def __init__(self,employeeID,department):
        self._empID=employeeID
        self._dept= department
    
    def getempiD(self):
        return self._empID

    def getDept(self):
        return self._dept

    def toString(self,):
        return self._empID,self._dept,person.getName(),person.getAddress()
