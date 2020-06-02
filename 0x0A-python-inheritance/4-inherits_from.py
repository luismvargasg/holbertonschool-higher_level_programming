#!/ust/bin/python3
"""Module to test an object"""


def inherits_from(obj, a_class):
    """function to test if object is an instance of a_class.

    Args:
        obj: object to test.
        a_class: specified class.

    Return:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class.
        False if object is not an instance.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
