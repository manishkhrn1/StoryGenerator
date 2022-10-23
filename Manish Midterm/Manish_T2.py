"""
My name is Manish Khurana
My student no. is 991705696
"""
def enterPassword():                                             #We declared a function called enterpassword()
    newPassword='b'                                              #We declared a string variable 'newPassword' and input a value to make it a little bit different than the value of confirmPassword
    confirmPassword = 'a'                                        # same with this variable
    while newPassword != confirmPassword:                               #we started a loop , so that until program meets this condition it will keep on asking the user
        newPassword=str(input("Enter a brand new-Password : "))         #here we again declared the newPassword variable , so that user can input)
        if(len(newPassword) >6 and len(newPassword)<10 ):                #Here we gave condition , so that the user input a password between 7 to 9 characters
            for char in newPassword:
                if char in ['#','@','%','*']:                               #here we started a loop to check the conditions, so that password contains a special character
                    confirmPassword=str(input("Re-Enter the Password : "))      #we again declared the confirmPassword variable , so that user can input
                    if confirmPassword==newPassword:
                        print("The new Password is: " , confirmPassword)                       
                    else:                                                           
                        print("Confirmed password does not match the original password !!")    

            if char not in ['#','@','%','*']:                                                               
                print("The password does not meet the password criteria - no special character ! ")                    #If the user is unable to meet with the special character condition,then this statement will be printed

        else:
            print("The password does not meet the password criteria - password is too short or too lengthy!")           #If the user is unable to meet with the length condition,then this statement will be printed


enterPassword()                                                                         #we used this statement to call the function
