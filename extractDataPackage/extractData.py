#Extract data.py

# Name: Cian R, Nosagie S, Jajuan H.
# email: roopnacn@mail.uc.edu, hill4ju@mail.uc.edu, @shermani@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/3/2024
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Call an API to communicate between softwares and print some interesting information from it.

# Brief Description of what this module does: This module calls the API from the URL and parses the data
# Citations:
# Anything else that's relevant:
import requests
import json


def extract_data():
    response = requests.get('https://randomuser.me/api/')
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    return parsed_json