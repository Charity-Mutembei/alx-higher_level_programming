#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    Open the file with the given filename in read
    mode using the 'utf8' encoding
    """
    with open(filename, 'r', encoding='utf8') as file:
        """
        Read the entire contents of the file and store
        it in the 'content' variable
        """
        for i in file:
            print(i, end="")
