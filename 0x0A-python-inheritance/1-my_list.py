#!/usr/bin/python3
"""Module to define a class Mylist"""


class MyList(list):
    """defining a class that inherits from list"""
    def __init__(self):
        """initializing MyList"""
        super().__init__()

    def print_sorted(self):
        """Method to print the list, but sorted (ascending sort)"""
        new_list = self[:]
        new_list.sort()
        print(new_list)
