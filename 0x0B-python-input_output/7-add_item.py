#!/usr/bin/python3
"""
a script that adds all arguments to
a Python list, and then save them to a file:
"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""remove the script name from the line arguments"""
argv.pop(0)


try:
    """Attempts the load of exisitng lists from file"""
    deserialized = load_from_json_file("add_item.json")
    if deserialized is None:
        """
        If the file is empty is non-existent,
        save command line arguments in a list
        """
        save_to_json_file(argv, "add_item.json")
    else:
        """
        if the file exists and has data, extend the
        existing list of command line arguments
        """
        deserialized.extend(argv)
        save_to_json_file(deserialized, "add_item.json")
except FileNotFoundError:
    """
    if the file is not found then create new and save command
    line argumets
    """
    save_to_json_file(argv, "add_item.json")
