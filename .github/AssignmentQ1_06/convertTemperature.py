def convertTemp(arrTemperature):
    arrConverted = []
    index = 0
    while(index < len(arrTemperature)):
        convertTemp = ( (arrTemperature[index] * (9/5)) + 32)
        arrConverted.append(convertTemp)
        index +=1
    
    return arrConverted

arrTemp = [50, 45,40,55,60,35]
print(f"The converted temperature list is {convertTemp(arrTemp)}")