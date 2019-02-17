factorial=1    #To store the factorial of a no.

num=int(input("Enter a no. whose factorial is needed:  "))   #Accepting a no. from user
if(num<0):
     print("Its an negative integer so factorial is not possible")
            #Checking for a negative integer entered from user
elif(num==0):
     print("Factorial of 0 is 1")
            #Factoral of zero is one
else:
    for i in range(1,num+1):
           factorial=factorial*i      #Storing factorial of the number
    factorial="{0:.2f}".format(factorial)
                #Mathematical function to store the number to two decimal place
    print("Factorial of a number",num,"is  ",factorial)    #Printing the factorial of the no.
