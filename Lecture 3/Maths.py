'''
x=int(input("please enter the value of x you wanna assign :"))
#sum = x - ((x**3)/3) + ((x**5)/5) - ((x**7)/7) + ((x**9)/9)

limit =int(input("Enter the number of limits you wanna add : "))
sum1 = -(x**(limit+2)/(limit+2) )
sum= 0
i=0

while (i!=limit):
    sum = x - sum1
    print(sum)

print(sum)
'''
sum = x - ((x**3)/3) + ((x**5)/5) - ((x**7)/7) + ((x**9)/9)
