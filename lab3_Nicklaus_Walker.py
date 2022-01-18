# -----------------------------------------------------------------------
# Nicklaus Walker
# Which lab this is – Lab 3
# This program takes the users first name, month born, and year born and
# checks if the user entered a valid input and decides if the user was
# born during a leap year or not.
# -----------------------------------------------------------------------


def main():
    # Name Input and declare variables x & y for future function use
    name = input("Enter Your First and Last Name: ")
    x = 0
    y = 0

    # Call functions...
    month_user_born = get_month(x)
    year_user_born = get_year(y)
    season_user_born = find_season(month_user_born)
    leap_year = is_leap_year(year_user_born)

    # Display Greeting
    if leap_year:
        print("\nHello, ", name, "! You were born in the ", season_user_born, " and ", year_user_born,
              " was a leap year.\n", sep='')
    else:
        print("\nHello, ", name, "! You were born in the ", season_user_born, " and ", year_user_born,
              " was not a leap year.\n", sep='')

    pennies = int(input("How many pennies are in your penny jar?: "))
    penny_jar(pennies)


#########################################
# Function Name: get_month
# Input: N/A
# Output: Returns month user born
# Purpose: Validates users input
#########################################
def get_month(x):
    valid = False

    while not valid:
        x = int(input("What Month were you born(Ex: Jan(1), Feb(2), etc.)?: "))

        if 12 > x < 1:
            print("Invalid Input. Must be 1-12")
            valid = False
        else:
            valid = True
            return x


#########################################
# Function Name: get_year
# Input: N/A
# Output: Returns year user born
# Purpose: Validates users input
#########################################
def get_year(y):
    valid = False

    while not valid:
        y = int(input("What Year were you born?: "))

        if y <= 0:
            print("Invalid Input.")
            valid = False
        else:
            valid = True
            return y


#########################################
# Function Name: find_season
# Input: month_user_born
# Output: Returns season_user_born
# Purpose: Check what season user was born
#########################################
def find_season(z):
    if z == 1 or z == 2 or z == 12:
        z = 'Winter'
    elif z == 3 or z == 4 or z == 5:
        z = 'Spring'
    elif z == 6 or z == 7 or z == 8:
        z = 'Summer'
    elif z == 9 or z == 10 or z == 11:
        z = 'Fall'
    return z


#########################################
# Function Name: is_leap_year
# Input: year_user_born
# Output: Returns leap_year True or False
# Purpose: Determines if year was leap year
#########################################
def is_leap_year(f):
    if (f % 4) == 0:
        if (f % 100) == 0:
            if (f % 400) == 0:
                f = True
            else:
                f = False
        else:
            f = True
    else:
        f = False

    return f


#########################################
# Function Name: penny_jar
# Input: pennies
# Output: Print Statement
# Purpose: Calculates the denomination user gets back
#########################################
def penny_jar(a):
    dollars = a // 100
    quarters = (a - (dollars * 100)) // 25
    dime = (a - (dollars * 100) - (quarters * 25)) // 10
    nickel = (a - (dollars * 100) - (quarters * 25) - (dime * 10)) // 5
    penny = (a - (dollars * 100) - (quarters * 25) - (dime * 10) - (nickel * 5))

    if dollars > 0:
        print(dollars, "dollars")
    if quarters > 0:
        print(quarters, "quarters")
    if dime > 0:
        print(dime, "dimes")
    if nickel > 0:
        print(nickel, "nickels")
    if penny > 0:
        print(penny, "pennies")


main()
