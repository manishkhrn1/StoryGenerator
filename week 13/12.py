#a = ['b']
#b= ['a','c']
#c= ['b']
#dict1 = {a:a,b:b,c:c}
#print(dict1)
"""
dict1={}
listA=[]
listA.append("b")

listB=[]
listB.append("a")
listB.append("c")

dict1["a"]=listA
dict1["b"]=listB
print(dict1)

for nei in dict1:
    print(dict1.get(nei))
    """

listStudents = [("Richard", 99 , "Will Pass") , ("Daniel", 45 , "Will not pass") , ("Rajiv",43), ("Tuffy",100,"Will Pass"),
("Golu",43,"Will not pass"),("Gandu" ,20), ("Dhruv",32)]

passingStud = {'Will pass': 0, 'Will not Pass' : 0}
for nei in listStudents:
    try:
    
        if nei[2] == "Will Pass":
            passingStud['Will pass'] +=1
        if nei[2] =="Will not pass": 
            passingStud["Will not Pass"]+=1 

    
    except Exception:
        print(nei[0] + "  Unknown if they/he/she will pass")

print(passingStud)