#principal = 10000
#TimesInterest= 12
#rate = 0.08


def totalAmount(principal, rate , TimesInterest ,time):
    amount = principal * (1 + rate/TimesInterest) ** (TimesInterest*time)
    return amount

enterTime= int(input("Enter the number of years you want to calculate for: "))
#total(enterTime)
print(totalAmount(10000,0.08,12,enterTime))