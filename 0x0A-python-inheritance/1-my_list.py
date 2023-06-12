#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
