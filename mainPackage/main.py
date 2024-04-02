#main.py

import requests
import json
from extractDataPackage import *
from extractDataPackage.extractData import extract_data
from extractDataPackage.pullInfo import extract_info
if __name__ == "__main__":
    
    dict = {}
    dict = extract_data()
    

    extract_info(dict)

   

