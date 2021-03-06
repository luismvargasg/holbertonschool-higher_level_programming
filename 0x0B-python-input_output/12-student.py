#!/usr/bin/python3
"""Module to create a class Student"""


class Student:
    """defining the class Student"""
    def __init__(self, first_name, last_name, age):
        """instantiation of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation
        of a Student.
        """
        my_dict = {}
        if type(attrs) == list and all([type(a) == str for a in attrs]):
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
            return my_dict
        else:
            return self.__dict__
