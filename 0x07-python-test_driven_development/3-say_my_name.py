#!/usr/bin/python
"""printing a name.

Usage Example:
say_my_name("Walter", "White")
"""


def say_my_name(first_name, last_name=""):
    """function that prints: My name is <first name> <last name>.

    Args:
        first_name: must be a string.
        last_name: must be a string.

    Returns:
         nothing.

    Raises:
        TypeError: if args != string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
