#!/usr/bin/python3
"""Defining the Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation
        of list_objs to a file.
        """
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(cls.to_dictionary(obj))
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation json_string.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attributes
        already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        objs = []
        try:
            with open(filename, mode="r", encoding="utf-8") as myFile:
                objs = cls.from_json_string(myFile.read())
            for key, value in enumerate(objs):
                objs[key] = cls.create(**objs[key])
        except:
            pass
        return objs
