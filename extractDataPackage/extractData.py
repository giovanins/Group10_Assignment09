#Extract data.py
import requests
import json


def extract_data():
    response = requests.get('https://randomuser.me/api/')
    json_string = response.content
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    return parsed_json