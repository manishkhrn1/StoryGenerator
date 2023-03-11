'''
try:
    fileRef = open("olympics.txt",'r')

    fileRef.close()
except Exception as e:
    print(e)
'''
'''
try:
    fileRef = open("school_prompt2.txt",'r')
    records = fileRef.read()
    print("File content :" + records)
    print(len(records))
    fileRef.close()
except Exception as e:
    print(e)
    '''
'''
with open ("travel_plans2.txt","r") as fileRef:
    numLines = len(fileRef.readlines())  #Returns a list
    print(fileRef.readlines())
    print(fileRef.readlines())
    fileRef.seek(0)
    print(fileRef.readlines())
    '''
'''
with open("emotion_words2.txt","r") as fileRef:
    print(fileRef.readline(9))
    '''
'''
with open("subfolder/olympics1.txt","r") as fileRef:
    record = fileRef.readline() #To skip the first line

    for line in fileRef:
        record = line.split(',')
        print(record[0] + " from " + record[3] + " is competing in the " + record[4] + " event")
'''
#write squared no for 1 ,2 ,.......,12 to a file named squared_no.txt
#For example:
#   1 squared : 1
#   2 squared : 4

with open("subfolder/squared_no.txt","a") as fileRef:
    for value in range(26,46):
        squaredValue = pow(value,2)
        fileRef.write(str(value)+ " squared: " + str(squaredValue) + "\n")
    """
    
try:
    fileRef = open("practice.txt",'r')
    records = fileRef.readline(30)
    print("File content :" + records)
    print(len(records))
    fileRef.close()
except Exception as e:
    print(e)"""