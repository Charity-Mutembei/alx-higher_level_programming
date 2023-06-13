#!/usr/bin/python3
"""
a function that appends a string at the end of a text file
(UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    Open the file with the given filename in
    append mode using the 'utf8' encoding
    """
    with open(filename, 'a', encoding='utf8') as file:
        """Write the text to the file"""
        file.write(text)

        """Return the number of characters added"""
        return len(text)
