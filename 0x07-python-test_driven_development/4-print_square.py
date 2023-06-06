#!/usr/bin/python3
"""
a function that prints a square with the character #.
"""


def print_square(size):
    """
    Print a square with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If `size` is not an integer or
        if `size` is a float less than 0.
        ValueError: If `size` is less than 0.

    Returns:
        None
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size.is_integer() and size >= 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
