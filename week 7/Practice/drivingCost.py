def DrivingCost(distance , miles , price):
    totalCost = (distance/miles) * price
    return totalCost

distance =float(input("Please Enter the total distance in miles that you have to cover : "))    
miles =float(input("Please Enter the total miles your vehicle can cover on a gallon of gas : "))
price =float(input("Please Enter the  price per gallon of gas : "))
cost = DrivingCost(distance,miles,price)
print("Total cost of driving would be :" , round(cost,2))