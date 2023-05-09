#!/usr/bin/python3
def islower(c):
    """
    Returns True if the given character is lowercase.
    Returns False otherwise.
    """
    # check if the character is between 'a' and 'z' in ASCII table
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
