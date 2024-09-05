def checkNum(number):
    if(number%2 == 0):
        print("Number is even and divisible by 2") # we are checking two things. One is disibility and second type of number (even or odd)
    else:
        if(number%3 == 0): #checking here if entered number is divisible by 3. adding it here to avoide code duplication. we can check it here as well
            print("Number is divisible by 3")

        print("Number is odd")
    
    if(number == 0):
        print("number is 0")
    elif(number > 0):
        print("number is positive")
    else:
        print("Number is negative")
        
    

numberToCheck = int(input("Please Enter Number: "))
checkNum(numberToCheck)