#!/usr/bin/python3
"""
function that finds the peak number in a list
"""


def find_peak(list_of_integers):
    """
    the function under questions
    Iterate through the list, excluding the first
    and last elements
    """
    length = len(list_of_integers)
    if length == 0:
        print("None")
    else:
        for i in range(1, len(list_of_integers) - 1):
            if list_of_integers[i] > list_of_integers[i - 1] and list_of_integers[i] > list_of_integers[i + 1]:
                print(f"{list_of_integers[i]}")
