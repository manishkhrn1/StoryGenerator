sentence= str(input("Please enter the sentence you wanna check alphabets and consonants for  : "))
vowels=['a','e','i','o','u']
count=0
totalLetters = 0

for i in sentence:
    totalLetters += 1
    if i in vowels:
        count += 1
        
print("Total vowels are : ", count)
print ("Total consonants are : ",totalLetters - count)