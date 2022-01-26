# -----------------------------------------------------------------------
# Which lab this is – Lab 1
# This program takes the users first name, month born, and year born and
# decides if the user was born during a leap year and what season
# -----------------------------------------------------------------------


# Define Variables
# Using the input function to get users input on user defined variables

name = input("Enter Your First and Last Name: ")
monthUserBorn = int(input("What Month were you born(Ex: Jan(1), Feb(2), etc.)?: "))
yearUserBorn = int(input("What Year were you born?: "))
seasonUserBorn = ''
isLeapYear = False

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
else:
    print("Invalid Input. Try Again")

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
    print("Hello, ", name, "! You were born in the ", seasonUserBorn, " and ", yearUserBorn, " was a leap year.", sep='')
else:
    print("Hello, ", name, "! You were born in the ", seasonUserBorn, " and ", yearUserBorn, " was not a leap year.", sep='')

