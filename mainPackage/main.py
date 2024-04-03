#main.py
# Name: Cian R, Nosagie S, Jajuan H.
# email: roopnacn@mail.uc.edu, hill4ju@mail.uc.edu, @shermani@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 04/3/2024
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Call an API to communicate between softwares and print some interesting information from it.

# Brief Description of what this module does. This is the entry point. The function is imported and called here to pull from the API data. 
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

   

