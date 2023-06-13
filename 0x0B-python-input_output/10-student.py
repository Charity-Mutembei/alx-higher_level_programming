#!/usr/bin/python3
"""
a class Student that defines a student by:
(based on 9-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age:
def __init__(self, first_name, last_name, age):
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given attributes.

        Args:
            first_name: First name of the student.
            last_name: Last name of the student.
            age: Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs: List of attribute names to retrieve (optional).

        Returns:
            A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)

        return result
