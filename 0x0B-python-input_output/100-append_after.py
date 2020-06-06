#!/usr/bin/python3
"""Module to def a function that inserts a line"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each
       line containing a specific string.

    Args:
        filename: given file to add the line.
        search_string: given string to look into the file.
        new_string: string to add after the matching result.
    """
    update_file = ""
    with open(filename, mode="r+") as myFile:
        for line in myFile:
            update_file += line
            if search_string in line:
                update_file += new_string
        myFile.seek(0)
        myFile.write(update_file)
