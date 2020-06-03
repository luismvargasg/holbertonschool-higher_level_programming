#!/usr/bin/python3
"""Module to append a string to a text file"""


def append_write(filename="", text=""):
    """function that appends a string to a text file (UTF8).

    Args:
        filename: text file to read.
        text: string to add in the text file.

    Return:
        the number of characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
