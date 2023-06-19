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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a file in JSON format
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation to a list
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
