#!/usr/bin/python3
"""Module to create a class"""


class BaseGeometry:
    """defining an empty class"""
    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method to validae received value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value

class Rectangle(BaseGeometry):
    """defining a class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instatiation of class Rectangle"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
