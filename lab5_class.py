class Contact:

    def __init__(self):
        # Initialize private variables
        self.__birthdate = ""
        self.__name = ""
        # Contact info variable
        self.contact_month = 0
        self.contact_year = 0

#########################################
# Function Name: get_name
# Input: N/A
# Output: returns state of self.__name
# Purpose: Accessor
#########################################
    def get_name(self):
        return self.__name

#########################################
# Function Name: get_birthdate
# Input: N/A
# Output: returns state of self.__birthdate
# Purpose: Accessor
#########################################
    def get_birthdate(self):
        return self.__birthdate

#########################################
# Function Name: set_name
# Input: N/A
# Output: N/A
# Purpose: Mutator
#########################################
    def set_name(self, contact_name):
        self.__name = contact_name

#########################################
# Function Name: set_birthdate
# Input: N/A
# Output: N/A
# Purpose: Mutator
#########################################
    def set_birthdate(self, contact_birthdate):
        self.__birthdate = contact_birthdate

#########################################
# Function Name: find_season
# Input: N/A
# Output: returns a string, season
# Purpose: Find the season the contact was born
#########################################
    def find_season(self):
        space = self.get_birthdate().index(" ")
        month = self.get_birthdate()[:space]

        if month == 1 or month == 2 or month == 12:
            season = 'Winter'
        elif month == 3 or month == 4 or month == 5:
            season = 'Spring'
        elif month == 6 or month == 7 or month == 8:
            season = 'Summer'
        else:
            season = 'Fall'

        return season

#########################################
# Function Name: calculate_age
# Input: current_date
# Output: age
# Purpose: slices contact & current date into
# integers and returns the age of the contact
#########################################
    def calculate_age(self, current_date):
        # Take contact birthdate and index position
        # of the first space and comma
        # slice string into integers and prepare to calculate
        space = self.__birthdate.index(" ")
        comma = self.__birthdate.index(",")
        contact_day = int(self.__birthdate[space:comma])
        self.contact_year = int(self.__birthdate[-4:])

        if "January" in self.__birthdate:
            self.contact_month = 1
        elif "February" in self.__birthdate:
            self.contact_month = 2
        elif "March" in self.__birthdate:
            self.contact_month = 3
        elif "April" in self.__birthdate:
            self.contact_month = 4
        elif "May" in self.__birthdate:
            self.contact_month = 5
        elif "June" in self.__birthdate:
            self.contact_month = 6
        elif "July" in self.__birthdate:
            self.contact_month = 7
        elif "August" in self.__birthdate:
            self.contact_month = 8
        elif "September" in self.__birthdate:
            self.contact_month = 9
        elif "October" in self.__birthdate:
            self.contact_month = 10
        elif "November" in self.__birthdate:
            self.contact_month = 11
        elif "December" in self.__birthdate:
            self.contact_month = 12

        # Take current date and index position
        # of the first space and comma
        # slice string into integers and prepare to calculate
        space = current_date.index(" ")
        comma = current_date.index(",")
        current_day = int(current_date[space:comma])
        current_year = int(current_date[-4:])

        if "January" in current_date:
            current_month = 1
        elif "February" in current_date:
            current_month = 2
        elif "March" in current_date:
            current_month = 3
        elif "April" in current_date:
            current_month = 4
        elif "May" in current_date:
            current_month = 5
        elif "June" in current_date:
            current_month = 6
        elif "July" in current_date:
            current_month = 7
        elif "August" in current_date:
            current_month = 8
        elif "September" in current_date:
            current_month = 9
        elif "October" in current_date:
            current_month = 10
        elif "November" in current_date:
            current_month = 11
        else:
            current_month = 12

        # Determine the age of the contact
        if (current_month, current_day) < (self.contact_month, contact_day):
            age = (current_year - self.contact_year) - 1
        else:
            age = current_year - self.contact_year

        return age

#########################################
# Function Name: is_lea_year
# Input: N/A
# Output: Boolean
# Purpose: Determine if the contact was born
# during a leap year or not
#########################################
    def is_leap_year(self):
        if self.contact_year % 4 == 0:
            if self.contact_year % 100 == 0:
                if self.contact_year % 400 == 0:
                    leap_year = True
                else:
                    leap_year = False
            else:
                leap_year = True
        else:
            leap_year = False

        return leap_year
