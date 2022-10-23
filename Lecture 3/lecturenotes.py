'''TODAY LECTURE FOCUSES ON IF-ELSE AND OTHER TYPES(E.G., NESTED IF-ELSE)'''    

#print(type(True))
#print(type("True"))

answer1 = True
answer2 = False

#print(answer1 or answer2)  # ||
#print(answer and answer2) # &&
#print(not answer1)      # !

#num = 8
#print(num > 0 and num < 100)
#print(num % 2 ==0 or num % 3 == 0 )

totalWeight = int(input('Enter total weight of luggage : '))
numpieces = int(input('Number of pieces: '))

#if ((totalWeight/numpieces) > 50):
if (numpieces != 0 and (totalWeight / numpieces) > 50):
    print('average weight is greater than 50 , so mate give me 50 bucks extra')

print ('YOu are good mate , have a good holiday')
