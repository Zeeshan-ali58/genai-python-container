def insertNewValues(arr, index, value):
    arr.insert(index, value)
    return arr

arrDummy = ["BMW","Merceds","Hyundai"]
callFunc = insertNewValues(arrDummy, 2, "Suzuki")
print(callFunc)