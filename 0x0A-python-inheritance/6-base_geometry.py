#!/usr/bin/python3
"""
a class BaseGeometry (based on 5-base_geometry.py)
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
