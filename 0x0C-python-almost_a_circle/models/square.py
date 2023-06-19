#!/usr/bin/python3
"""
Square class that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size attribute (same as width)
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size attribute (same as width)
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
