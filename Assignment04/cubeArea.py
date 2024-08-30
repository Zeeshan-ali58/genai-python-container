import math
def calculateCubeArea(sideOfCube):
    sidesOfCube = 6
    circleArea = sidesOfCube * (sideOfCube**2)
    print(f"circle area is {circleArea:.2f} units")

sideOfCube = float(input("Enter diameter of circle: "))
calculateCubeArea(sideOfCube)



