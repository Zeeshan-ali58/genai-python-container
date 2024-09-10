def calculateFactorial(number):
    fact = 1
    while(number >= 1):
        fact = fact * number
        number -=1
    return fact

print(calculateFactorial(5))
