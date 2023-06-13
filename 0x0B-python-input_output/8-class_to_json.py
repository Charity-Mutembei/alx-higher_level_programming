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
        A dictionary representation of the object suitable
        for JSON serialization.
    """
    if isinstance(obj, dict):
        """
        If the object is a dictionary, recursively convert
        its values to JSON-serializable dictionaries
        """
        return {k: class_to_json(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        """
        If the object is a list, recursively convert its
        elements to JSON-serializable dictionaries
        """
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, (str, int, bool)):
        """
        If the object is a string, integer, or boolean, return it directly
        """
        return obj
    else:
        """For other data types, raise an exception or handle them as needed"""
        raise ValueError("Object of unsupported type encountered.")
