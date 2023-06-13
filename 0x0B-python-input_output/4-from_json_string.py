#!/usr/bin/python3
"""
function that returns an object (Python data structure)
represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """Convert the JSON string to a Python data structure"""
    obj = json.loads(my_str)

    return obj
