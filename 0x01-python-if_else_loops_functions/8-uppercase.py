#!/usr/bin/python3
def uppercase(s):
    """
    Prints the given string in uppercase followed by a new line.
    """
    # initialize an empty string for the uppercase version
    uppercase_s = ''

    # loop through each character in the string
    for c in s:
        # check if the character is lowercase
        if ord(c) >= 97 and ord(c) <= 122:
            # convert lowercase character to uppercase by subtracting 32
            # from its ASCII value
            uppercase_c = chr(ord(c) - 32)
        else:
            # if the character is not lowercase, use the original character
            uppercase_c = c
        # append the uppercase character to the uppercase string
        uppercase_s += uppercase_c

    # print the uppercase string followed by a new line using string format
    print("{}".format(uppercase_s))
