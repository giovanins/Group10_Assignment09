#main.py
# Name: Cian Roopnarine, JaJuan Hill, Nosagie Sherman
# email: roopnacn@mail.uc.edu, hill4ju@mail.uc.edu, shermani@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 3/28/24
# Course/Section: IS 4010 Section 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: We collaborated with our group members to execute an API using an URL.

# Brief Description of what this module does: this is the main, it runs the function
# Citations:
# Anything else that's relevant:

import requests
import json
from extractDataPackage import *
from extractDataPackage.extractData import extract_data
from extractDataPackage.pullInfo import extract_info
if __name__ == "__main__":
    
    dict = {}
    dict = extract_data()
    

    extract_info(dict)

   

