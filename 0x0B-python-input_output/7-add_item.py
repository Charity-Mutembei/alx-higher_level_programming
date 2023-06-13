#!/usr/bin/python3
"""
a script that adds all arguments to
a Python list, and then save them to a file:
"""
import sys
import json


def save_to_json_file(data, filename):
    """
    Saves the given data as JSON to the specified file.

    Args:
        data: The data to be saved as JSON.
        filename: The name of the file to save the data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_from_json_file(filename):
    """
    Loads JSON data from the specified file and returns it.

    Args:
        filename: The name of the file to load JSON data from.

    Returns:
        The loaded JSON data.
    """
    with open(filename, 'r') as file:
        return json.load(file)


"""
Get the command line arguments excluding the script name
"""
arguments = sys.argv[1:]

try:
    """Attempt to load existing list from file"""
    existing_list = load_from_json_file("add_item.json")
    if existing_list is None:
        existing_list = []

    """Extend the existing list with the command line arguments"""
    existing_list.extend(arguments)

    """Save the updated list to the file"""
    save_to_json_file(existing_list, "add_item.json")
except FileNotFoundError:
    """
    If file not found, create a new file and
    save the command line arguments as a list
    """
    save_to_json_file(arguments, "add_item.json")
