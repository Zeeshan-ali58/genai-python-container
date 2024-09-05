import calendar

def checkDaysAndLeapYear(month, year):
    isLeap = calendar.isleap(year)
    daysInMonth = calendar.monthrange(year, month)[1]

    print(f"Year {year} is a leap year: {isLeap}")
    print(f"Month {month} has {daysInMonth} days")

month = int(input("Enter month number: "))
year = int(input("Enter year number: "))
checkDaysAndLeapYear(month, year)