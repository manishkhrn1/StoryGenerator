resps =[0,0,0,0]
x=int(input("what's the percentage of rain : "))
percent_rain = [x>=90, 80<=x<90, 50<=x<80, 0<=x<50 ]

if(percent_rain[0]):
    
   # Output = ('Bring an Umbrella')
    #resps[0] = 'Bring an Umbrella'
    resps += [('Bring an Umbrella')]
elif(percent_rain[1]):
    resps +=  ["Good for the flowers?"]
    #print("Good for the flowers?")
elif(percent_rain[2]):
    resps += ["Watch out for clouds"]
    #print("Watch out for clouds") 
elif(percent_rain[3]):
     resps += ["have a good day"]
    #print("have a good day")
print(resps)