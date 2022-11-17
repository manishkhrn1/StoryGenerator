
from random import randint

class Player:
    def __init__(self,name,):
        self.name = name
        self.guess = -1

    def getName(self):
        return self.name
    def getNumber(self):
        return self.guess
    def play(self):
        guessNumber= guessNumber.randint(0,9)
        self.guess=guessNumber
randomNumber = randint(0,9)
larry=Player("Larry")
curly=Player("Curly",randomNumber)
moe=Player("Moe",randomNumber)
print(larry.getName() , "chooses" , larry.getNumber())
