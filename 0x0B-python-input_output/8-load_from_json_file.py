#!/usr/bin/python3
"""Module to create an object from JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file

    Args:
        filename: file to be read the object.
    """
    with open(filename, encoding="utf-8") as myFile:
        return json.load(myFile)
