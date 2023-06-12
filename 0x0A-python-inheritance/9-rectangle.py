#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """below is the constructor"""
    def __init__(self, width, height):
        """the width and height must be positive"""
        self.integer_validator("width", width)
        self.pos_width = width
        """check the height"""
        self.integer_validator("height", height)
        self.pos_height = height

    """the area() method must be implemented"""
    def area(self):
        return self.pos_width * self.pos_height

    "the string part"
    def __str__(self):
        return f"[Rectangle] {self.pos_width}/{self.pos_height}"
