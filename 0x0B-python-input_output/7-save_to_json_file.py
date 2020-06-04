#!/usr/bin/python3
"""Module to return an object"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
       using a JSON representation.

    Args:
        my_obj: Given objet.
        filename: file to be write.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(json.dumps(my_obj))
