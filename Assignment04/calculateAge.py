from datetime import datetime,timedelta
def calculateAge():
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

#call the function
calculateAge()
