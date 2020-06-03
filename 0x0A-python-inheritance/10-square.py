#!/usr/bin/python3
"""Module to create a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defining a class that inherits from Rectangle"""
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)

    def area(self):
        """method to find the area of Square"""
        return self.__size * self.__size

    def __str__(self):
        """returning the string representation of the object"""
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
