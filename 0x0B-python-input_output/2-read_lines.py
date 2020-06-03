#!/usr/bin/python3
"""Module to read n lines text file"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file (UTF8)
       and prints it to stdout.

    Args:
        filename: text file to read.
        nb_lines:
    """
    with open(filename) as myFile:
        lines = myFile.readlines()
    if nb_lines <= 0 or nb_lines >= len(lines):
        nb_lines = len(lines)
    for i in range(nb_lines):
        print(lines[i], end="")
