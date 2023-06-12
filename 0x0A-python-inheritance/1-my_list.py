#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        for element in sorted_list:
            print(element, end=' ')
        print()
