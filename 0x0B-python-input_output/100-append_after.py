#!/usr/bin/python3
"""
a function that inserts a line of text to a file,
after each line containing a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing
    a specific string in a file.

    Args:
        filename: Name of the file.
        search_string: String to search for in each line.
        new_string: Line of text to insert after each matched line.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
