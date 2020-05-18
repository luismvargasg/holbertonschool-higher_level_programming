#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True # if value has been printed (it means is an integer)
    except:
        return False # if value is not an integer.
