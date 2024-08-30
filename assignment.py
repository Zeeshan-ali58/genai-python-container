from datetime import datetime,timedelta
import math
#calculating age on years month and days
dob = datetime(1992, 6, 29)
current_date = datetime.now()

dobYears = current_date.year - dob.year 
dobMonths =current_date.month - dob.month
dobDays =current_date.day - dob.day

if dobDays < 0:
    dobDays -=1
    daysInPrevMonth = (current_date.replace(day=1) - timedelta(days=1)).day
    dobDays += daysInPrevMonth

if dobMonths < 0:
    dobYears -=1
    dobMonths += 12

print(f"You are {dobYears} years, {dobMonths} months, and {dobDays} days old.")

# now we'll be calculating the area of rectangle
recLength = 15
recWidth = 10
recArea = recLength * recWidth
print(f"The areas of rectagle us {recArea} unit squares")

# now we'll be calculating the area of circle
diameter = 100
radius = 100/2
circleArea = math.pi * (radius**2)
print(f"Area of circle is {circleArea:.2f}")

# now we'll be calculating the area of cube
cubeSides = 6 # a cube has six sides
sideArea = 10
cubeArea = 6 * (sideArea**2)
print(f"Area of cube is {cubeArea}")

# now we'll be calculating the volume of cylinder
cycilderRadius = 5
cylinderHeight = 20
cylinderVolume = math.pi * (cycilderRadius**2) * cylinderHeight
print(f"Volume of cylinder is {cylinderVolume:.2f}")

#calculating BMI (Body mass index). Formuls is squre of weight/heighnt in meters
heightInMeters = 5 * 0.3048 # 0.3048 unit in meters against 1 foot
heightInInches = 7 * 0.0254
height =heightInMeters + heightInInches
weight = 84
bmiCalculation = weight/ height**2
print(f"My BMI according to height and weight is {bmiCalculation:.2f}")


# now we'll be converting seconds into minutes
totalSeconds = 3600 
secondsInOneMinute = 60
calculateInMinutes = int(totalSeconds/secondsInOneMinute)
print(f"There are {calculateInMinutes} minutes according of {totalSeconds} seconds" )


# now we'll be converting temperature from fahrenheit to celcius and vise versa
tempInCelcius = 48 
tempInFahrenheit = tempInCelcius * (9/5) + 32
tempInCelciusReConvert = (tempInFahrenheit -32) * 5/9
print(f"Temperature in Fahrenheit is {tempInFahrenheit} and by converting Fahrenheit into Celcius the result is {tempInCelciusReConvert}" )


#calculating percentage
obtainedMarks = 840
totalMarks = 1050
calculatePercentage = (obtainedMarks/totalMarks) * 100
print(f"Total obtained marrks percentage is {calculatePercentage:.2f} percentage" )
