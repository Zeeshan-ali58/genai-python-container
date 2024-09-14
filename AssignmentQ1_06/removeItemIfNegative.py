def removingItemFromArr(arr,value):
    if(value in arr and value < 0):
        arr.remove(value)
    return arr

arrItems = [1,2,-3,4,6]
rmItem = removingItemFromArr(arrItems,-3)
print(rmItem)

#Second method to remove is by iteration

def removingItemFromArrByLoop(arr,value):
    index = 0
    while index < len(arr):
        if(arr[index] == value and value < 0):
            arr.remove(arr[index])
        index +=1
    return arr

arrItems01 = [1,2,-3,-4,6,10,23,-45]
rmItem = removingItemFromArrByLoop(arrItems01,-4)
print(rmItem)