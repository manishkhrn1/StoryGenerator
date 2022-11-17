"""class DefaultArguments:
    def printInfo(self,name,age=19):
       # This prints a passed info into this method 
           It uses keyword arguments
        

        print("Name: ",name )
        print("Age : ",age)

app = DefaultArguments()
app.printInfo(name = "Rajiv")
"""
class DefaultArguments:
    def printInfo(self,name,age=19):
        """This prints a passed info into this method 
           It uses keyword arguments
        """

        print("Name: ",name )
        print("Age : ",age)
    
    def sum(self,*numbers):
        sum = 0
        for n in numbers:
            sum+= n
        return sum 

app = DefaultArguments()
app.printInfo(name = "Rajiv")
print(app.sum(1,2,3,4,5,6,7,8))