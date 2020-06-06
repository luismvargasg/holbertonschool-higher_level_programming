#!/usr/bin/python3
"""module to matrices multiplication"""
from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices.

    Args:
        m_a: first matrix, must be an list of lists of integers or floats.
        m_a: second matrix, must be an list of lists of integers or floats.

    Returns:
        new matrix with the result of the multiplication.

    Raises:
        TypeError: if m_a or m_b is not a list.
        TypeError: if m_a or m_b is not a list of lists.
        ValueError: if m_a or m_b is empty / = [] or = [[]]
        TypeError: if one element of those list is not and int or float.
        TypeError: if m_a or m_b is not a rectangle / != row size.
        ValueError: if m_a or m_b can´t ve multiplied.
    """
    return matmul(m_a, m_b)
