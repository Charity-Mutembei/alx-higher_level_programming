#!/usr/bin/python3
"""
a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry():
    """the method below is an instance"""
    """the constructor intialize empty"""
    def __init__(self) -> None:
        pass

    """the method below raises expection"""

    def area(self):
        """returns message below"""
        raise Exception("area() is not implemented")

    """the method validates value"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer". format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0". format(name))
