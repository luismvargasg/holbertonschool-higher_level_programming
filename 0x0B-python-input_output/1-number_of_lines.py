#!/usr/bin/python3
"""Module to count the number of lines in a text file"""


def number_of_lines(filename=""):
    """function that returns the number of lines
       of a text file.

    Args:
        filename: text file to read.

    Return:
        number of lines.
    """
    count = 0
    with open(filename) as myFile:
        for lines in enumerate(myFile):
            count += 1
    return count
