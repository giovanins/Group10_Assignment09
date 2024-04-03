#pullinfo

# Name: Cian R, Nosagie S, Jajuan H.
# email: roopnacn@mail.uc.edu, hill4ju@mail.uc.edu, @shermani@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/3/2024
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Call an API to communicate between softwares and print some interesting information from it.

# Brief Description of what this module does: Creates a dictionary of the dictionary data from the API
# Citations:
# Anything else that's relevant:
def extract_info (dict):
    new_dict = dict['results']
    dicton = new_dict[0]
    name_dict = dicton['name']
    location_dict = dicton['location']
    country_dict = location_dict['country']
    
    print("Our API generates a random person and gives information about them.")
    print("For this example our random person's name is: ", name_dict["title"], name_dict["first"], name_dict["last"])
    print("Their gender is: ", dicton['gender'])
    print("They are from: ", country_dict)