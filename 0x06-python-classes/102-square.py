#!/usr/bin/python3
"""
class Square that defines a square by: (based on 4-square.py)
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        size (property): Retrieve the size of the square.
        size (setter): Set the size of the square.
        area(): Calculate and return the area of the square.
        __eq__(): Compare two squares for equality.
        __ne__(): Compare two squares for inequality.
        __gt__(): Compare if a square is greater than another square.
        __ge__(): Compare if a square is greater than or equal to
        another square.
        __lt__(): Compare if a square is less than another square.
        __le__(): Compare if a square is less than or equal to another square.
    """

    def __init__(self, size=0):
        """
        Initialize a square with an optional size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If the size is not a number (float or integer).
            ValueError: If the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If the size is not a number (float or integer).
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two squares for equality.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compare two squares for inequality.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compare if a square is greater than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Compare if a square is greater than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is greater or equal,
            False otherwise.
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        Compare if a square is less than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compare if a square is less than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square is less or equal, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)
