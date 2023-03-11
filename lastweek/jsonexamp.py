import json
"""
person= '{"name": "Bob", "languages":["English", "French"]}'
print(type(person))

#In order to parse a Json format, we will convert it to Dict
personDict = json.loads(person)
print(type(personDict))
print(personDict['languages'])
"""
"""
with open('subfolder/person1.json','r') as fileRef:
    data = json.load(fileRef)
    print(data)
"""
'''
#convert Dict to Json
personDict = {'name': 'Bob' , 'age' :12 , 'Children': False}
personJson= json.dumps(personDict)
print(personJson)
'''
"""
#writing json to txt
personDict ={"name": 'Bob','languages':("English","French"),"married":True, "age":32    }
with open('person.txt','w') as jsonFile:
    json.dump(personDict,jsonFile)

#Read a Json file
with open ('person.txt', 'r') as fileRef:
    data = json.load(fileRef)
    print(data)"""