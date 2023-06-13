#!/usr/bin/python3
"""
a function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object:
"""


def class_to_json(obj):
    """
    Converts an object to a JSON-serializable dictionary.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the object
        suitable for JSON serialization.
    """
    i = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            i[key] = value

    return i
