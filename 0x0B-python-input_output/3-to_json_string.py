#!/usr/bin/python3
"""
function that returns the JSON
representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """Convert the object to a JSON string representation"""
    json_string = json.dumps(my_obj)

    return json_string
