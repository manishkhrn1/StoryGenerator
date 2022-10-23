from random import randint
dice= randint(2,12)
print("Welcome to the Games of Dice")
print("Here rules are Simple:")
print("you have to guess the possible number we can get if we roll two dices(You have to Guess the total sum)")
print("So let's begin : ")
guess = 0
        
while guess != dice:

    num = int(input( "Guess the possible number: "))
    guess = num

    if guess == dice:
          print("Congratulations , You win ") 
    elif (guess> dice and num <13):
        print("Too high ")     
    elif (guess< dice and num > 1):
            print ( "Too low")
    elif (guess>12 or guess<2) :
            print("It's not a possible no. , sum of two dices ranges from 2 to 12, try again please")
print("Game over!, thanks for playing")            