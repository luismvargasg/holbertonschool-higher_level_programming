#!/usr/bin/python3
"""Module to repr an obj as JSON"""
import json


def to_json_string(my_obj):
    """function that make a JSON repr.

    Args:
        my_obj: object to represent.

    Return:
        the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
