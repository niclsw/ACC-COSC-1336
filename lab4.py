# -----------------------------------------------------------------------
# Which lab this is – Lab 4
# This program loads contactsLab4.txt and separates it's values into 2
# lists. It then determines the age and if the contact was born during
# a leap year.
# -----------------------------------------------------------------------


def main():
    # Initialize lists
    names_list = []
    birthdates_list = []

    # Try to open contactsLab4.txt, throw exception if not found
    try:
        # Initialize contacts_file
        contacts_file = open("contactsLab4.txt", 'r')

        # Begin reading lines from contacts lab into lists
        # strip out \n in all lines
        name = contacts_file.readline()
        while name != "":
            names_list.append(name.rstrip("\n"))
            date = contacts_file.readline()
            birthdates_list.append(date.rstrip("\n"))
            name = contacts_file.readline()

        # No longer need to file, close it
        contacts_file.close()

        # Get current date for variable current_date
        current_date = input("Enter the current date in the format m/dd/yyyy: ")

        # call function display_contacts
        display_contacts(names_list, birthdates_list, current_date)

    # Exception for file contactsLab4.txt not found
    except FileNotFoundError:
        print("File contactsLab4.txt does not exist")


#########################################
# Function Name: display_contacts
# Input: names_list, birthdates_list, current_date
# Output: N/A
# Purpose: Display a formatted version of contacts
#########################################
def display_contacts(names_list, birthdates_list, current_date):
    # Placeholders for width format
    other_width = '10'
    name_width = '23'
    age_total = 0

    # Display contact list with format
    print(
        format("Name", name_width),
        format("Age", other_width),
        format("Season", other_width),
        format("Leap Year", other_width)
    )
    print(
        format("-----", name_width),
        format("-----", other_width),
        format("-----", other_width),
        format("-----", other_width)
    )

    # Run for loop to print each line in a parallel list
    for i in range(len(names_list)):
        # Calculate age total
        age = get_age(birthdates_list[i], current_date)
        age_total += age

        # Print name, age(string), season, and leap year for each contact
        print(
            format(names_list[i], name_width),
            format(str(get_age(birthdates_list[i], current_date)), other_width),
            format(find_season(birthdates_list[i]), other_width),
            is_leap_year(birthdates_list[i])
            )

    # Print average age of contact list
    print("\nAverage age of contact list is: ", int(age_total / len(names_list)))


#########################################
# Function Name: find_season
# Input: birthday_input
# Output: season
# Purpose: take contacts birthday and determine the season the contact was born
#########################################
def find_season(birthday_input):
    # Take input of birthday and split to obtain the month contact was born
    # Convert string to integer to allow if statements to determine the season
    month = birthday_input.split("/", 3)
    month = int(month[0])

    # Determine what season contact was born
    if month == 1 or month == 2 or month == 12:
        season = 'Winter'
    elif month == 3 or month == 4 or month == 5:
        season = 'Spring'
    elif month == 6 or month == 7 or month == 8:
        season = 'Summer'
    else:
        season = 'Fall'
    # Return the string season
    return season


#########################################
# Function Name: is_leap_year
# Input: birthday_input
# Output: Returns leap_year True or False
# Purpose: Isolate birth year and determine if it is a leap year
#########################################
def is_leap_year(birthday_input):
    # Take birthday input and split the string into a list with 3 parts
    # Convert the year/part 3 to int
    birthday_year = birthday_input.split("/", 3)
    birthday_year = int(birthday_year[-1])

    if birthday_year % 4 == 0:
        if birthday_year % 100 == 0:
            if birthday_year % 400 == 0:
                leap_year = "Yes"
            else:
                leap_year = "No"
        else:
            leap_year = "Yes"
    else:
        leap_year = "No"

    # Return a boolean value
    return leap_year


#########################################
# Function Name: get_age
# Input: birthday_input & current_date_input
# Output: returns age
# Purpose: Isolate birth y/m/d and current y/m/d and determine the age of the contact
#########################################
def get_age(birthday_input, current_date_input):
    # Separate current_date_input into 3 integers to calculate the age of the contact
    current_date_list = current_date_input.split("/")
    current_date_month = int(current_date_list[0])
    current_date_day = int(current_date_list[1])
    current_date_year = int(current_date_list[2])

    # Separate birthday_input into 3 integers to calculate the age of the contact
    birthday_date_list = birthday_input.split("/", 3)
    birthday_date_month = int(birthday_date_list[0])
    birthday_date_day = int(birthday_date_list[1])
    birthday_date_year = int(birthday_date_list[2])

    # calculates the contact's age
    if (current_date_month, current_date_day) < (birthday_date_month, birthday_date_day):
        age = (current_date_year - birthday_date_year) - 1
    else:
        age = current_date_year - birthday_date_year

    return age


main()
