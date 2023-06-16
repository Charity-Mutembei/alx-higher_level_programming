#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project
"""


class Base():
    """Private class __nb_objects"""
    __nb_objects = 0
    """having a constructor below"""
    def __init__(self, id=None):
        """if id is not none == id is argument"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
