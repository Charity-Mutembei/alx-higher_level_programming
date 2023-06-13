#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Read the contents of the JSON file"""
    with open(filename, 'r') as file:
        json_string = file.read()

    """Parse the JSON string and create the object"""
    obj = json.loads(json_string)

    return obj
