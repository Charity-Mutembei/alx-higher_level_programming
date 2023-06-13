#!/usr/bin/python3
"""
a function that adds a new attribute to an object if
it’s possible:
"""


def add_attribute(obj, attr_name, attr_value):
    """lets if this works mahn"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    obj.__setattr__(attr_name, attr_value)
