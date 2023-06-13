#!/usr/bin/python3
import json
"""
function that returns the JSON
representation of an object (string):
"""


def to_json_string(my_obj):
    """Convert the object to a JSON string representation"""
    json_string = json.dumps(my_obj)

    return json_string
