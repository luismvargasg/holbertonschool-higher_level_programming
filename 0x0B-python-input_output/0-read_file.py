#!/usr/bin/python3
"""Module to read a text file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and
        prints it to stdout.

    Args:
        filename: text file to read.
    """
    with open(filename) as myFile:
        print(myFile.read(), end="")
