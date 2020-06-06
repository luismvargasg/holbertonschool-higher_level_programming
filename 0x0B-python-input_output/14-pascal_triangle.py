#!/usr/bin/python3
"""Module to represent the Pascal's triangle"""


def pascal_triangle(n):
    """function that returns a list of lists of integers
       representing the Pascals triangle of n.

    Args:
        n: given number to represent.

    Return:
        an empty list if n <= 0 or the triangle.
    """
    pt = []  # pt = Pascal Triangle
    if n > 0:
        for i in range(n):
            pt.append([])
            pt[i].append(1)
            for j in range(1, i):
                pt[i].append(pt[i - 1][j - 1] + pt[i - 1][j])
            if i is not 0:
                pt[i].append(1)
    return pt
