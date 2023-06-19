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

    def to_csv_row(self):
        """
        Convert instance attributes to a CSV row
        """
        if self.__class__.__name__ == "Rectangle":
            return [self.id, self.width, self.height, self.x, self.y]
        elif self.__class__.__name__ == "Square":
            return [self.id, self.size, self.x, self.y]
        return []

    @staticmethod
    def from_csv_row(row):
        """
        Convert a CSV row to instance attributes
        """
        if len(row) == 0:
            return {}
        if row[0] == "Rectangle":
            keys = ["id", "width", "height", "x", "y"]
        elif row[0] == "Square":
            keys = ["id", "size", "x", "y"]
        return dict(zip(keys, row[1:]))
