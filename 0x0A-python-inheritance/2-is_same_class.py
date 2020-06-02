#!/ust/bin/python3
"""Module to test an object"""


def is_same_class(obj, a_class):
    """function to test if object is exactly an instance o a_class.

    Args:
        obj: object to test.
        a_class: specified class.

    Return:
        True if the object is exactly an instance of the specified class.
        False if object is not an instance..
    """
    return type(obj) is a_class
