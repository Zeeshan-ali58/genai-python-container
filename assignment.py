from datetime import datetime,timedelta

dob = datetime(1992, 6, 29)
current_date = datetime.now()

age_years = current_date.year - dob.year
age_months = current_date.month - dob.month
age_days = current_date.day - dob.day

# Adjust for cases where the current month or day is before the birth month or day
if age_days < 0:
    age_months -= 1
    days_in_prev_month = (current_date.replace(day=1) - timedelta(days=1)).day
    age_days += days_in_prev_month

if age_months < 0:
    age_years -= 1
    age_months += 12

# Print the result
print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")
