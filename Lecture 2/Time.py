seconds = int(input("Please input the seconds you wanna convert in actual human time : "))
minutes = seconds//60
minutes1= minutes%60
hours = minutes//60
secondsLeft = seconds%60


#print(minutes)
#print(hours)
print(hours,":", minutes1, ":", secondsLeft)