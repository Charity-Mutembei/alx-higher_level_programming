#!/usr/bin/python3
"""
class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a square with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
