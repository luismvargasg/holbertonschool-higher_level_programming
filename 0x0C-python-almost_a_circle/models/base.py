#!/usr/bin/python3
"""Defining the Base class"""


class Base:
    """This class will be the base of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor for Base.

        Args:
            id: is an integer, if id is not None, id with this argument
            value is assigned, otherwise __nb_objects is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
