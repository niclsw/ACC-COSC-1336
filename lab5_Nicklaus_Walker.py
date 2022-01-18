import lab5_class_Walker


#########################################
# Function Name: main
# Input: N/A
# Output: N/A
# Purpose: Read from contact file and place data in contact object
#########################################
def main():
    # Initialize contact list variable
    contact_list = []

    # Try to open contactsLab5.txt
    # Throw exception if file not found
    try:
        # Open File contactsLab5.txt
        contacts_file = open('contactsLab5.txt', 'r')

        # Being reading lines from file and append to contact_list
        name = contacts_file.readline().rstrip("\n")
        while name != "":
            birthday = contacts_file.readline().rstrip("\n")

            # Create object and set name and birthday element
            contact = lab5_class_Walker.Contact()
            contact.set_name(name)
            contact.set_birthdate(birthday)

            contact_list.append(contact)
            name = contacts_file.readline().rstrip("\n")

        # Close Contact file
        contacts_file.close()

        # Send contact_list to display contacts
        display_contacts(contact_list)



    except FileNotFoundError:
        print("contactsLab5.txt Not Found!")


#########################################
# Function Name: display_contacts
# Input: contact_list, current_date
# Output: N/A
# Purpose: Display a formatted version of contacts
#########################################
def display_contacts(contact_list):
    # Initialize Age Total
    age_total = 0
    # Placeholders for width format
    other_width = '12'
    name_width = '23'

    # Get current_date from user
    current_date = input("Enter Current Date (Month DD, Year): ")

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

    # For loop to run through index of contact_list
    # Each iteration by 2 to prevent index error
    for i in range(len(contact_list)):
        # Send contact name & birthdate to contact object
        name = contact_list[i].get_name()
        season = contact_list[i].find_season()
        age = contact_list[i].calculate_age(current_date)

        if contact_list[i].is_leap_year():
            leap_year = "Yes"
        else:
            leap_year = "No"

        # Print age, season, and is leap year
        print(
            format(name, name_width),
            format(str(age), other_width),
            format(season, other_width),
            format(leap_year, other_width)
            )

        # Accumulator for age total
        age_total += age

    # Print average age of contact list
    print("\nAverage age of contact list is: ", int(age_total / (len(contact_list) / 2)))


main()
