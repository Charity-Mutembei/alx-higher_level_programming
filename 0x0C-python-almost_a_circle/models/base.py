#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project
"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set using a dictionary
        """
        if cls.__name__ == "Rectangle":
            """Create a dummy instance with arbitrary dimensions"""
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            """Create a dummy instance with arbitrary size"""
            dummy = cls(1)
        else:
            """Create a dummy instance of other classes"""
            dummy = cls()
        """Use the update method to set the real values"""
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a file and return a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                obj_list = cls.from_json_string(json_data)
                instance_list = [cls.create(**obj) for obj in obj_list]
                return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to CSV file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is not None and len(list_objs) > 0:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                writer.writerow(fields)
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())
            else:
                writer.writerow([])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from CSV file
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                instance_list = []
                for row in reader:
                    instance = cls.create(**row)
                    instance_list.append(instance)
                return instance_list
        except FileNotFoundError:
            return []
