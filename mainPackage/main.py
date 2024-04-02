#main.py

import requests
import json
from extractDataPackage import *
from extractDataPackage.extractData import extract_data
if __name__ == "__main__":
    
    dict = {}
    dict = extract_data()
    print(dict)
