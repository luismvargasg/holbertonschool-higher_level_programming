#!/usr/bin/python3
"""Module to create a class Student"""


class Student:
    """defining the class Student"""
    def __init__(self, first_name, last_name, age):
        """instantiation of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary representation
        of a Student.
        """
        return self.__dict__
