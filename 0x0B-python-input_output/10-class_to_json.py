#!/usr/bin/python3
"""Module containing a function that returns a dictionary"""


def class_to_json(obj):
    """function that returns the dictionary description
       with simple data structure.

    Args:
        obj: is an instance of a Class.

    Return:
        A dictionary, (list, dictionary, string, integer and boolean)
        for JSON serialization of an object.
    """
    return obj.__dict__
