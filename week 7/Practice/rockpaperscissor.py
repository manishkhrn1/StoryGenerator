from random import randint

choose=randint(0,2)


number=0
#while number != 3:
    #number += 1
num = int(input("Scissors : 0 , rock : 1 , paper : 2 , please choose one of them : "))

if num<=2:
    if(choose == 0):
        if (num == 0):
            print("The computer is scissor and you are scissors as well . It is a draw ")
        elif (num == 1):
            print("The computer is scissor and you are rock . You win ")    
        elif (num == 2):
            print("The computer is scissor and you are paper . You lose ")
        else:
            print("enter a valid entry : ")    
    if(choose == 1):
        if (num == 0):
            print("The computer is rock and you are scissors  . you lose ")
        elif (num == 1):
            print("The computer is rock and you are rock as well . it is a draw ")    
        elif (num == 2):
            print("The computer is rock and you are paper . You win ")
        else:
            print("enter a valid entry : ")    
    if(choose == 2):
        if (num == 0):
            print("The computer is paper and you are scissors  . you win ")
        elif (num == 1):
            print("The computer is paper and you are rock  . you lose  ")    
        elif (num == 2):
            print("The computer is paper and you are paper as well . it is a draw ")      
else:
    print("enter a valid entry : ")  