#!/usr/bin/python3
"""
A function that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    :param m_a: The first matrix.
    :type m_a: list[list[int or float]]
    :param m_b: The second matrix.
    :type m_b: list[list[int or float]]
    :return: The result of matrix multiplication.
    :rtype: list[list[int or float]]
    :raises TypeError: If m_a or m_b is not a list
    or if m_a or m_b is not a list of lists.
    :raises ValueError: If m_a is empty or if m_b is empty
    or if the number of columns in m_a is not equal to the
    number of rows in m_b or if the rows of m_a or m_b have different sizes.
    """

    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")
    if m_a == [] or m_b == []:
        raise ValueError("m_a can't be empty and m_b can't be empty")
    if any(not isinstance(num, (int, float)) for row in m_a for num in row) or \
            any(not isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats and m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size and each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)

    return result

