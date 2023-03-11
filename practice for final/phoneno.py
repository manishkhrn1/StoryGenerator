from random import randint

#num=randint(0,9)
num1=randint(6,9)

#phone=[num1,num,num,num,num,num,num,num,num,num]
#print("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(phone[0],phone[1],phone[2],phone[3],phone[4],phone[5],phone[6],phone[7],phone[8],phone[9]))
phoneNo= []
for i in range (9):
    num=randint(0,9)
    #print(i)
    phoneNo.append(num)

print("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}".format(num1,phoneNo[0],phoneNo[1],phoneNo[2],phoneNo[3],phoneNo[4],phoneNo[5],phoneNo[6],phoneNo[7],phoneNo[8]))
