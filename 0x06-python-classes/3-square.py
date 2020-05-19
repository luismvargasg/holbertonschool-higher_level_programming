#!/usr/bin/python3
class Square:
    """Defines a square

    Attribute:
        size: (:obj: `int`, optional): private instance.
        area: (:obj: `int`, optional): public instance.

    Raises:
        TypeError: An exception if parameter size is not an integer.
        ValueError: An exception if parameter size is less than 0.
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
