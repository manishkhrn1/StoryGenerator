class KeywordsArguments:
    def printInfo(self,name,age):
        """This prints a passed info into this method 
           It uses keyword arguments
        """

        print("Name: ",name )
        print("Age : ",age)

app = KeywordsArguments()
age = 30
name = "John"

app.printInfo(age=30,name="John")