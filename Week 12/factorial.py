def calculateFact(number):
    if number ==0:
        return 1
    else:
        recursiveStep = calculateFact(number-1)
        result = recursiveStep * number
        return result

inputNum = int(input("Please enter the number you want factorial for :"))
result = calculateFact(inputNum)
print("The Result of the factorail is :", result)