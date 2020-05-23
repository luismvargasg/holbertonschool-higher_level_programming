#!/usr/bin/python3
"""function to print a text."""


def text_indentation(text):
    """prints a text with 2 new lines after each
    of these characters: ., ? and :.
    Args:
        text: must be a string.
    Returns:
         nothing.
    Raises:
        TypeError: if text is not a string.
    """
    flag = 0
    string = ""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if flag == 1 and i == " ":
            string += ""
            flag == 2
        elif flag == 2 and i == " ":
            string += ""
        elif i in [".", "?", ":"]:
            flag = 1
            string += i + "\n\n"
        else:
            string += i
            flag = 0
    print(string, end="")
