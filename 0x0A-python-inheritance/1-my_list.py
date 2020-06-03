#!/usr/bin/python3
"""Module to define a class Mylist"""


class MyList(list):
    """defining a class that inherits from list"""

    def print_sorted(self):
        """Method to print the list, but sorted (ascending sort)"""
        print(sorted(self))
