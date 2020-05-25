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
    def width(self):
        """getter for attribute width"""
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
    def height(self):
        """getter for attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """define the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """define the perimeter of the rectangle"""
        if self.__width > 0 and self.__height > 0:
            return (self.__width + self.__height) * 2
        else:
            return 0
