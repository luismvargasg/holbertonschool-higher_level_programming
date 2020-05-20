#!/usr/bin/python3
"""defining MagicClass Attributes: area and circumference."""
import math


class MagicClass:
    """defining MagicClass"""
    def __init__(self, radius=0):
        """initializing radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """defining area"""
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """defining circumference"""
        return 2 * math.pi * self.__radius
