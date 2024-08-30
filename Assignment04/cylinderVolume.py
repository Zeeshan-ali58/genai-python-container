import math
def calculateCylinderVolume(cycilderRadius, cylinderHeight):
    cycilderRadius = 5
    cylinderHeight = 20
    cylinderVolume = math.pi * (cycilderRadius**2) * cylinderHeight
    print(f"Volume of cylinder is {cylinderVolume:.2f}")\


cycilderRadius = float(input("Enter radius of cylinder: "))
cylinderHeight = float(input("Enter height of circle: "))
calculateCylinderVolume(cycilderRadius, cylinderHeight)