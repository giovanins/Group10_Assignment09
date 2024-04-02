#pullInfro.py
# Name: Cian Roopnarine, JaJuan Hill, Nosagie Sherman
# email: roopnacn@mail.uc.edu, hill4ju@mail.uc.edu, shermani@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 3/28/24
# Course/Section: IS 4010 Section 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: We collaborated with our group members to execute an API using an URL.

# Brief Description of what this module does: This module pulls the needed information from the extracted data
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