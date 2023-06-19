#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Call the superclass constructor with id, x, y,
        size for width and height"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
