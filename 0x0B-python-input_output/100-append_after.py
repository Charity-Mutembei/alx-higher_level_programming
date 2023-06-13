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
    modified_lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            modified_lines.append(line)
            if search_string in line:
                modified_lines.append(new_string + '\n')

    with open(filename, 'w') as file:
        file.writelines(modified_lines)
