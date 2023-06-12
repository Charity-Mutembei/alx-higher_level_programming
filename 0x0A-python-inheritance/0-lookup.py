#!/usr/bin/python3
"""
function that returns the list of available
attributes and methods of an object:
"""


def lookup(obj):
    # Create an empty list to store the attributes and methods
    result = []

    # Retrieve the list of all attributes and methods of the object
    attributes_and_methods = dir(obj)

    # Iterate over each attribute or method name
    for attr in attributes_and_methods:
        # Check if the attribute or method name does not start with '__'
        if not attr.startswith('__'):
            # Add the attribute or method name to the result list
            result.append(attr)

    # Return the final list of attributes and methods
    return result
