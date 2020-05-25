#!/usr/bin/python3
"""module to define a rectangle"""


class Rectangle:
    """defines a rectangle.

    Args:
        width: (int) optional.
        height: (int) optional.

    Atributes:
        width: (int) optional.
        height: (int) optional.
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    """getter for attribute width"""
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("witdh must be >= 0")
        else:
            self.__width = value

    @property
    """getter for attribute height"""
    def heigth(self):
        return self.__height

    @width.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
