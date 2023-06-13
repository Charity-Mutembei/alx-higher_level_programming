#!/usr/bin/python3
"""
a function that writes a string to a text file
(UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    Open the file with the given filename in write mode
    using the 'utf8' encoding
    """
    with open(filename, 'w', encoding='utf8') as file:
        """Write the text to the file"""
        file.write(text)

        """Return the number of characters written"""
        return len(text)
