def calculatePercentage(obtainedMarks, totalMarks):
    if(obtainedMarks > totalMarks):
        print("Error: Obtained marks should be less than total marks")
        return False
    
    calculatePercentage = (obtainedMarks/totalMarks) * 100
    print(f"Total obtained marrks percentage is {calculatePercentage:.2f} percentage" )

obtainedMarks = int(input("Enter obtained marks: "))
totalMarks = int(input("Enter total marks: "))
calculatePercentage(obtainedMarks, totalMarks)