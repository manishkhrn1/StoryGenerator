def isLeapYear(year):
   
    if (year %4 == 0 and year%100 != 0):
        print("yes it is a leap year")

    elif(year %4 == 0 and year%100 == 0)and(year%400 ==0):
        print("yes it is  a leap year")
    else:
        print("No")     

year= int(input("Please Input the year : "))
askForYear= isLeapYear(year)