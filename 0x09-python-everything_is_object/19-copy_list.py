#!/usr/bin/python3
"""module to copy a list"""


def copy_list(l):
    """defining a function to copy a list.

    Args:
        l: received list.

    Return:
        the copy of a list
    """
    new_l = l[:]
    return new_l
