import math
def calculateRectanegleArea(recLength, recWidth):
    
    recArea = recLength * recWidth
    print(f"The areas of rectagle us {recArea:.2f} unit squares")

recLength = float(input("Enter length:"))
recWidth = float(input("Enter width:"))
calculateRectanegleArea(recLength,recWidth)