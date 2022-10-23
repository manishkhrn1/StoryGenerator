from random import randint     #We Imported a Library called Random where it gives us option to get a random no.
dice= randint(2,12)            #Here we called the method radint (2,12), we used the following numbers because 2 it is minimum possibilty and 12 is the maximum possibility
print("Welcome to the Games of Dice")
print("Here rules are Simple:")
print("you have 3 Chances to guess the possible number we can get if we roll two dices(You have to Guess the total sum)")
#print("If you guess it right, Then you will get 10 Dollars")
#print("Else you will lose 2 dollars per game")
#print("So let's begin")
guess = 0 
chance = 0

#while chance != 3:
        
while guess != dice and chance != 3 :                  # We are starting a loop such that it will keep on asking the user about the number until or unless they guess the right no. and used 'chance' to let user have 3 chances

    num = int(input( "Guess the possible number: "))
    guess = num

    if guess == dice:
          print("Congratulations , You win here are your 10 bucks") 
    elif (guess> dice and num <13):
        print("Too high ")
        chance = chance + 1
        print("You have" , (3-chance) , "chances left " )
        if chance ==3:
            print("Sorry! You have used all of your chances")        
    elif (guess< dice and num > 1):
            print ( "Too low")
            chance = chance + 1
            print("You have" , (3-chance) , "chances left " )
            if chance ==3:
                print("Sorry! You have used all of your chances")
    elif (guess>12 or guess<2) :
            print("It's not a possible no. , sum of two dices ranges from 2 to 12, try again please")
print("game over, thanks for playing")            