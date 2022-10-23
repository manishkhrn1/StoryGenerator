class Interest():
    def __init__(self,years):
        self.principal = 10000
        self.rate = 0.08
        self.NumberOfTimes = 12
        
        

years= int(input("Please Enter the number of years : "))
obj = Interest(years)
totalAmount = obj.principal * (1+(obj.rate/obj.NumberOfTimes))**(obj.NumberOfTimes * years)        
print(totalAmount)

