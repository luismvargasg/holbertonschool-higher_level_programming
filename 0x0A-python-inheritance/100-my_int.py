#!/usr/bin/python3
"""Module to create a class MyInt"""


class MyInt(int):
    """defining a class MyInt that inherits from int.

    MyInt is a rebel. MyInt has == and != operators inverted.
    """
    def __eq__(self, num):
        """method to return the opposite result of comparation"""
        return int(self) != num

    def __ne__(self, num):
        """method to return the opposite result of comparation"""
        return int(self) == num
