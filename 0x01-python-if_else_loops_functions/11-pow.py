#!/usr/bin/python3
def pow(a, b):
    """
    Returns the value of a raised to the power of b.
    """
    result = 1
    for i in range(abs(b)):
        result *= a
    if b < 0:
        result = 1 / result
    return result
