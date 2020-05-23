#!/usr/bin/python3
"""function to print a square.

Usage example:
print_square(2)
##
##
"""


def print_square(size):
    """function that prints a square with the character #.
    Args:
        size: must be an integer, is the size length of the square.

    Returns:
         nothing.

    Raises:
        ValueError: if size is less than 0.
        TypeError: if size is a float and is less than 0.
        TypeError: if size is not an integer.
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        print("#" * size)
