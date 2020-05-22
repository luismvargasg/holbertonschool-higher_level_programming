#!/usr/bin/python3
"""Integers addition.

Usage example:
print(add_integer(4, 8))

"""


def add_integer(a, b=98):
    """function that adds 2 integers, a and b must be first
       casted to integers if they are float.

    Args:
        a: must be integer or float.
        b: must be integer or float.

    Returns:
         an integer: the addition of a and b.

    Raises:
        TypeError: a and b must be integers or floats,
        otherwise raise a TypeError exception with the message
        a must be an integer or b must be an integer.

    """
    c = 0
    if type(a) not in [int, float] or a != a or a == float("inf"):
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b != b or b == float("inf"):
        raise TypeError("b must be an integer")
    else:
        c = int(a) + int(b)
        return c
