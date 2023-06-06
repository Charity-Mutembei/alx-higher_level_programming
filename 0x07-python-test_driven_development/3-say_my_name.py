#!/usr/bin/python3
"""
a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Print the name using the provided first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
