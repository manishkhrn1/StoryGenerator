#We are importing sheridan Class which has the required objects to run the program
from SheridanSystem import SheridanSystem                                       
class Application:       
    #This method will import the sheridan class method run , that will run the program                                                           
    def start(self):
        sheridanObj = SheridanSystem()
        sheridanObj.run()

applicationObj = Application()  #We created the object applicationObj, which is an object of the class
applicationObj.start() #This object is going to call the method from application class