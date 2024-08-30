def convertMinutesAndSeconds(totalSeconds, secondsInOneMinute):
    calculateInMinutes = int(totalSeconds/secondsInOneMinute)
    print(f"There are {calculateInMinutes} minutes according of {totalSeconds} seconds" )

totalSeconds = int(input("Enter seconds to convert: "))
secondsInOneMinute = int(input("Enter minutes to convert: "))
convertMinutesAndSeconds(totalSeconds, secondsInOneMinute)