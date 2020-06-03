#!/usr/bin/python3
"""Module to create a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defining a class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instatiation of class Rectangle"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
