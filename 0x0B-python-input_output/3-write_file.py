#!/usr/bin/python3
"""Module to write a string to a text file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8).

    Args:
        filename: text file to read.
        text: string to add in the text file.

    Return:
        the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
