#!/usr/bin/python3
import numpy as np
"""
a function that multiplies 2 matrices by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    :param m_a: First matrix
    :type m_a: list of lists
    :param m_b: Second matrix
    :type m_b: list of lists
    :return: Result of matrix multiplication
    :rtype: numpy.ndarray
    """
    # Convert matrices to NumPy arrays
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    # Perform matrix multiplication using NumPy's dot product
    result = np.dot(np_a, np_b)

    return result.tolist()
