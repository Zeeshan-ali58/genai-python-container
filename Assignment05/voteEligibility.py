def checkVoteEligibility(age):
    if(age >=18):
        nationality = str(input("Enter Nationality: "))
        if(nationality.title() == 'Pakistani'):
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")
    else:
        print("You are under age")

userAge = int(input("Enter age in years: "))
checkVoteEligibility(userAge)