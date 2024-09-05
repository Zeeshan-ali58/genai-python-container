"""
    In this program i am going to take date of birth instead of direct age in years. 
    We will calculate age in years and then will decide the seniority of citizen
"""
from datetime import datetime
def decideSeniority(dob):
    try:
        current_date = datetime.now()
        dateOfBirth = datetime.strptime(dob, "%d-%m-%Y")
        ageInYears = current_date.year - dateOfBirth.year
        if(ageInYears > 0 and ageInYears <= 12):
            print("Citizen is a child")
        elif(ageInYears >= 13 and ageInYears < 19):
            print("Citizen is teenager")
        elif(ageInYears >= 20 and ageInYears < 59):
            print("Citizen is adult")
        else:
            print("Person is senior citizen ")

    except ValueError:
        print("Invalid format! Please enter the date of birth in the format DD-MM-YYYY.")

dateOfBirth = str(input("Enter your age like (DD-MM-YY): "))
decideSeniority(dateOfBirth)