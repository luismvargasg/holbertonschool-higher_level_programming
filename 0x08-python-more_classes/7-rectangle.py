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
        number_of_instances: (int) counter for instances.
        print_symbol: Used as symbol for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    def __str__(self):
        """method to print the rectangle with the character #"""
        string = ""
        if self.__width > 0 and self.__height > 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    string += str(self.print_symbol)
                if h < self.__height - 1:
                    string += '\n'
        return string

    def __repr__(self):
        """representation of the object rectangle"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """getter for attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for attribute height"""
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
