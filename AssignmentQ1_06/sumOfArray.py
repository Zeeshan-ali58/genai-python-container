def calculateSumOfArray(array):
    index = 0 
    sum = 0
    while(index < len(array)):
        sum += array[index] 
        index +=1

    print(f"The sum of array items is {sum}")
    
arrToSum = [1,2,3,4,5]
calculateSumOfArray(arrToSum)
