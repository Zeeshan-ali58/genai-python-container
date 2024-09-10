def removeOddNumbers(arr):
    index = 0
    while(index < len(arr)):
        if(arr[index] % 2 != 0):
            arr.remove(arr[index])
        else:
            index += 1  
    return arr

arrToChk = [1,3,4,6,8]
prnt = removeOddNumbers(arrToChk)
print(f"print is {prnt}")