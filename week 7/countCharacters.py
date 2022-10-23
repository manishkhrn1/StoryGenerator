#def countCharacter(words):
    #for extractChar in words:
        #character=0
        #character+=1
        #print("No. of Characters are : ", character)

words=["water", "chair"]
#result= countCharacter(words[0])
#result2=countCharacter(words[1])
character=0
for extractChar in words:
     character= len(extractChar)
     print("No. of Characters are : ", character)