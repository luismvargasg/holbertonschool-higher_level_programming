#!/usr/bin/python3
"""Module to define the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defining the class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the Rectangle.
        Return:
           [Square] (<id>) <x>/<y> - <size>
        """
        string = "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size)
        return string

    @property
    def size(self):
        """getter for the private instance attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the private instance attribute size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """public method that assigns a key/value argument to each attribute"""
        if args is None or not args:
            for att_name, att_value in kwargs.items():
                setattr(self, att_name, att_value)
        else:
            att_name = ["id", "size", "x", "y"]
            att_value = []
            for arg in args:
                att_value.append(arg)
                for i in range(len(att_value)):
                    setattr(self, att_name[i], att_value[i])

    def to_dictionary(self):
        """public method that returns the dictionary representation
        of a Square.
        """
        myDict = {"id": self.id, "size": self.size, "x": self.x,
                  "y": self.y}
        return myDict
