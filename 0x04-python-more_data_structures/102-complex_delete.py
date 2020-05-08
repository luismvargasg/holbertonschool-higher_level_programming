#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp_dictionary = a_dictionary.copy()
    for key, val in temp_dictionary.items():
        if val == value:
            del a_dictionary[key]
    return a_dictionary
