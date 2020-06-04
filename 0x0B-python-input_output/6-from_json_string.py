#!/usr/bin/python3
"""Module to return an object"""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
       represented by a JSON string.

    Args:
        my_str: JSON string..

    Return:
        the object.
    """
    return json.loads(my_str)
