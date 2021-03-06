# 0x04. Python - More Data Structures: Set, Dictionary

> This directory contains all the tasks of the project "0x04. Python - More Data Structures: Set, Dictionary".

> Project made at [Holberton School](https://www.holbertonschool.com "Holberton School.") for educational purpose.

## General Objectives

* What are set and how to use them.
* What are the most common methods of set and how to use them.
* When to use sets versus lists.
* How to iterate into a set.
* What are dictionary and how to use them.
* When to use dictionaries versus lists or sets.
* What is a key in a dictionary.
* How to iterate into a dictionary.
* What is a lambda function.
* What is map, reduce and map functions.

## Basic info

### Sets
Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary.

### Dictionaries
Another useful data type built into Python is the dictionary (see Mapping Types  dict). Dictionaries are sometimes found in other languages as associative memories or associative arrays. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You cant use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().

It is best to think of a dictionary as an unordered set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.

Performing list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary, in arbitrary order (if you want it sorted, just use sorted(d.keys()) instead). [2] To check whether a single key is in the dictionary, use the in keyword.

For more information please visit:
* [Data Structures](https://docs.python.org/3.4/tutorial/datastructures.html)
* [Lambda, filter, reduce and map](https://www.python-course.eu/python3_lambda.php)

## Directory Files

| **File** | **Description** |
|----------|-----------------|
| [0. Squared simple](./0-square_matrix_simple.py) | Write a function that computes the square value of all integers of a matrix. |
| [1. Search and replace](./1-search_replace.py) | Write a function that replaces all occurrences of an element by another in a new list. |
| [2. Unique addition](./2-uniq_add.py) | Write a function that adds all unique integers in a list (only once for each integer). |
| [3. Present in both](./3-common_elements.py) | Write a function that returns a set of common elements in two sets. |
| [4. Only differents](/.4-only_diff_elements.py) | Write a function that returns a set of all elements present in only one set. | 
| [5. Number of keys](./5-number_keys.py) | Write a function that returns the number of keys in a dictionary. |
| [6. Print sorted dictionary](./6-print_sorted_dictionary.py) | Write a function that prints a dictionary by ordered keys. |
| [7. Update dictionary](./7-update_dictionary.py) | Write a function that replaces or adds key/value in a dictionary. |
| [8. Simple delete by key](./8-simple_delete.py) | Write a function that deletes a key in a dictionary. |
| [9. Multiply by 2](./9-multiply_by_2.py) | Write a function that returns a new dictionary with all values multiplied by 2 |
| [10. Best score](./10-best_score.py) | Write a function that returns a key with the biggest integer value. |
| [11. Multiply by using map](./11-mutiply_list_map.py) | Write a function that returns a list with all values multiplied by a number without using any loops. |
| [12. Roman to Integer](./12-roman_to_int.py) | Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer. |
| [13. Weighted average!](./100-weight_average.py) | Write a function that returns the weighted average of all integers tuple (<score>, <weight>) |
| [14. Squared by using map](./101-square_matrix_map.py) | Write a function that computes the square value of all integers of a matrix using map |
| [15. Delete by value](./102-complex_delete.py) | Write a function that deletes keys with a specific value in a dictionary. |
| [16. CPython #1: PyBytesObject](./103-python.c) | Create two C functions that print some basic info about Python lists and Python bytes objects. |

## Author

* [GitHub - Luis Miguel Vargas](https://github.com/luismvargasg)

* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)