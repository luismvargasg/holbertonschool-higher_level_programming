#!/usr/bin/python3
"""Module to define the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor fot class Rectangle

        Args:
            width: must be an integer, define the width of Rectangle.
            height: must be an integer, define the width of Rectangle.
            x:
            y:
            id: is an integer.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """getter for the private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the private instance attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """getter for the private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the private instance attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """defining the public method to find the area of Rectangle

        Return:
            Area value of the Rectangle, integer.
        """
        return self.width * self.height

    def display(self):
        """defining the public method that prints in stdout the
           Rectangle instance with the character #.
        """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """string representation of the Rectangle.

        Return:
           [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height)
        return string

    def update(self, *args, **kwargs):
        """public method that assigns a key/value argument to each attribute"""
        if args is None or not args:
            for att_name, att_value in kwargs.items():
                setattr(self, att_name, att_value)
        else:
            att_name = ["id", "width", "height", "x", "y"]
            att_value = []
            for arg in args:
                att_value.append(arg)
                for i in range(len(att_value)):
                    setattr(self, att_name[i], att_value[i])

    def to_dictionary(self):
        """public method that returns the dictionary representation
        of a Rectangle.
        """
        myDict = {"id": self.id, "width": self.width, "height": self.height,
                  "x": self.x, "y": self.y}
        return myDict
