import lab5_class_Walker


#########################################
# Function Name: display_contacts
# Input: contact_list, current_date
# Output: N/A
# Purpose: Display a formatted version of contacts
#########################################
def display_contacts(current_date, contact_list):
    # Initialize Contacts
    contact_obj = lab5_class_Walker.Contact()
    # Initialize Age Total
    age_total = 0
    # Placeholders for width format
    other_width = '12'
    name_width = '23'

    # Display contact list with format
    print(
        format("Name", '15'),
        format("Age", '5'),
        format("Season", '5'),
        format("Leap Year", '5')
    )
    print(
        format("-----", '15'),
        format("-----", '5'),
        format("-----", '5'),
        format("-----", '5')
    )

    # For loop to run through index of contact_list
    # Each iteration by 2 to prevent index error
    for i in range(0, len(contact_list), 2):
        # Send contact name & birthdate to contact object
        contact_obj.set_name(contact_list[i])
        print(format(contact_obj.get_name(), name_width), end="")
        contact_obj.set_birthdate(contact_list[i+1])

        # Print age, season, and is leap year
        print(
            format(str(contact_obj.calculate_age(current_date)), other_width),
            format(contact_obj.find_season(), other_width),
            format(contact_obj.is_leap_year(), other_width)
            )

        age_total += contact_obj.calculate_age(current_date)

    # Print average age of contact list
    print("\nAverage age of contact list is: ", int(age_total / (len(contact_list) / 2)))


def main():
    # Initialize contact list variable
    contact_list = []

    # Try to open contactsLab5.txt
    # Throw exception if file not found
    try:
        # Open File contactsLab5.txt
        contacts_file = open('contactsLab5.txt', 'r')

        # Being reading lines from file and append to contact_list
        line = contacts_file.readline().rstrip("\n")
        while line != "":
            contact_list.append(line)
            line = contacts_file.readline().rstrip("\n")

        # Take current_date input and send list + current date
        # to display_contacts function
        current_date = input("Enter Current Date: ")
        display_contacts(current_date, contact_list)

        # Ain't nobody need this file open anymore!
        contacts_file.close()

    except FileNotFoundError:
        print("contactsLab5.txt Not Found!")


main()
