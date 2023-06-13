#!/usr/bin/python3
"""
a function that writes an Object to a
text file, using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """Convert the object to a JSON string representation"""
    json_string = json.dumps(my_obj)

    """Write the JSON string to the file"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
