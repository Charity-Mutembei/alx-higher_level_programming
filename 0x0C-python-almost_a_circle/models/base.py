#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
