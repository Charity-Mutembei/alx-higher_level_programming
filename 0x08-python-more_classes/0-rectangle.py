#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle:
You are not allowed to import any module
"""


class Rectangle:
    def __init__(self, length=0, width=0):
        """
        Initialize a rectangle with given length and width.
        Default values are set to 0 if no arguments are provided.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.length * self.width

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)

    def __repr__(self):
        """
        Return a string representation of the Rectangle class instance.
        """
        return f"<class '0-rectangle.Rectangle'>\n{{}}"
