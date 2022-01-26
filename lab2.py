# -----------------------------------------------------------------------
# Which lab this is – Lab 2
# This program takes the users first name, month born, and year born and
# checks if the user entered a valid input and decides if the user was
# born during a leap year or not. Using sentinel 'zzz'
# -----------------------------------------------------------------------


# Define Variables
# Using the input function to get users input on user defined variables

name = input("Enter Your First and Last Name: ")
seasonUserBorn = ''
isLeapYear = False
zzz = ''

# Check if the user entered valid month/year

monthUserBorn = int(input("What Month were you born(Ex: Jan(1), Feb(2), etc.)?: "))

yearUserBorn = int(input("What Year were you born?: "))

while zzz != "zzz":
    if monthUserBorn < 1 or monthUserBorn > 12:
        monthUserBorn = int(input("Please enter a valid month (1-12): "))

    if yearUserBorn <= 0:
        yearUserBorn = int(input("Please enter a valid year: "))

    if yearUserBorn > 0 and 1 < monthUserBorn < 12:
        zzz = input("\nEnter 'zzz' to continue...")

# Determine what season user was born
# seasonUserBorn is used to keep track of the users born season

if monthUserBorn == 1 or monthUserBorn == 2 or monthUserBorn == 12:
    seasonUserBorn = 'Winter'
elif monthUserBorn == 3 or monthUserBorn == 4 or monthUserBorn == 5:
    seasonUserBorn = 'Spring'
elif monthUserBorn == 6 or monthUserBorn == 7 or monthUserBorn == 8:
    seasonUserBorn = 'Summer'
elif monthUserBorn == 9 or monthUserBorn == 10 or monthUserBorn == 11:
    seasonUserBorn = 'Fall'

# Decide if the user was born during a leap year
# Set bool isLeapYear to True or False

if (yearUserBorn % 4) == 0:
    if (yearUserBorn % 100) == 0:
        if (yearUserBorn % 400) == 0:
            isLeapYear = False
        else:
            isLeapYear = True
    else:
        isLeapYear = True
else:
    isLeapYear = False

# Print outputs if isLeapYear is 'True' else if 'false'
# Print whether user was born during a leap year

if isLeapYear:
    print("\nHello, ", name, "! You were born in the ", seasonUserBorn, " and ", yearUserBorn, " was a leap year.", sep='')
else:
    print("\nHello, ", name, "! You were born in the ", seasonUserBorn, " and ", yearUserBorn, " was not a leap year.", sep='')
