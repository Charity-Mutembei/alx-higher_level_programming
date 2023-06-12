#!/usr/bin/python3
"""
a class Square that inherits from Rectangle
(9-rectangle.py). (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the constructor below intializes"""
    def __init__(self, size):
        self.integer_validator("size", size)
        """we make sure its positive"""
        self.pos_size = size
        """the area"""
        super().__init__(self.pos_size, self.pos_size)

    """lets destroy the string method"""
    def __str__(self):
        return f"[Square] {self.pos_width}/{self.pos_height}"
