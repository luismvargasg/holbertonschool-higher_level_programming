#!/usr/bin/python3
"""Function to add new attribute to an object."""


def add_attribute(obj, att_name, att_value):
    """function that adds a new attribute to an object if its possible.

    Args:
        obj: Given Object.
        att_name: Name of the attribute to add in the object.
        att_value: Value to store in the new attribute.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, att_name, att_value)
    else:
        raise TypeError("can't add new attribute")
