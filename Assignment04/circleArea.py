import math
def calculateCircleArea(diameter):
    radius = diameter/2
    circleArea = math.pi * (radius**2)
    print(f"circle area is {circleArea:.2f} units")

diameterOfCircle = float(input("Enter diameter of circle: "))
calculateCircleArea(diameterOfCircle)



