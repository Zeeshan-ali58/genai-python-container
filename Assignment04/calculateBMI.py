import math
def calculateBmi(meters, inches, bodyWeight):
    heightInMeters = meters * 0.3048 # 0.3048 unit in meters against 1 foot
    heightInInches = inches * 0.0254
    height =heightInMeters + heightInInches
    bmiCalculation = bodyWeight/ height**2
    print(f"My BMI according to height and weight is {bmiCalculation:.2f}")

heightInMeters = int(input("Enter height in meters: "))
heightInInches = int(input("Enter height in inches: "))
weight = float(input("Enter height of circle: "))
calculateBmi(heightInMeters, heightInInches, weight)