def palindrome(word):
    #word=word.lower()
    length =len(word)  # if it is 5
    length2 = length-(length-1)   #If its value to be 1  , 5=1 , 4=2 , 3=3 str
    if (length//2)==0:
        recursStep = palindrome( ) 
    else:
        recursStep = palindrome(word[0])

        




enterWord=str(input("Please enter the word to check whether it is a palindrome or not "))
result = palindrome(enterWord)
if result ==1:
    print("Yes {0} is a palindrome ".format(enterWord))
else:
    print("No {0} is not a palindrome".format(enterWord))