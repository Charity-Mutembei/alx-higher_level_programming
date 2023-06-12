#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""


class Rectangle (BaseGeometry):
    """below is the constructor"""
    def __init__(self, width, height):
        """the width and height must be positive"""
        self.integer_validator("width", width)
        self.width = width
        """check the height"""
        self.integer_validator("height", height)
        self.height = height
