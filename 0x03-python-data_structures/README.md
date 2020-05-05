# 0x03. Python - Data Structures: Lists, Tuples

> This directory contains all the tasks of the project "0x03. Python - Data Structures: Lists, Tuples".

> Project made at [Holberton School](https://www.holbertonschool.com "Holberton School.") for educational purpose.

## General Objectives

* What are lists and how to use them.
* What are the differences and similarities between strings and lists.
* What are the most common methods of lists and how to use them.
* How to use lists as stacks and queues.
* What are list comprehensions and how to use them.
* What are tuples and how to use them.
* When to use tuples versus lists.
* What is a sequence.
* What is tuple packing.
* What is sequence unpacking.
* What is the del statement and how to use it.

## Basic info

One of the most versatile data types in Python is the list, it can be written as a list of comma-separated values (items) between square brackets.
```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```
Lists might contain items of different types, but usually the items all have the same type.
Like strings (and all other built-in sequence type), lists can be indexed and sliced:
```
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```
All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:
```
>>> squares[:]
[1, 4, 9, 16, 25]
```
Lists also support operations like concatenation:
```
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
For more information please visit: [list tutorial](https://docs.python.org/3.4/tutorial/introduction.html#lists)

## Directory Files

| **File** | **Description** |
|----------|-----------------|
| [0. Print a list of integers](./0-print_list_integer.py) | Write a function that prints all integers of a list. |
| [1. Secure access to an element in a list ](.1-element_at.py)) | Write a function that retrieves an element from a list like in C. |
| [2. Replace element](./2-replace_in_list.py) | Write a function that replaces an element of a list at a specific position (like in C). |
| [3. Print a list of integers... in reverse!](./3-print_reversed_list_integer.py) | Write a function that prints all integers of a list, in reverse order. |
| [4. Replace in a copy](./4-new_in_list.py) | Write a function that replaces an element in a list at a specific position without modifying the original list (like in C). |
| [5. Can you C me now?](./5-no_c.py) | Write a function that removes all characters c and C from a string. | 
| [6. Lists of lists = Matrix](./6-print_matrix_integer.py) | Write a function that prints a matrix of integers. |
| [7. Tuples addition](./7-add_tuple.py) | Write a function that adds 2 tuples. |
| [8. More returns!](./8-multiple_returns.py) | Write a function that returns a tuple with the length of a string and its first character. |
| [9. Find the max](./9-max_integer.py) | Write a function that finds the biggest integer of a list.  |
| [10. Only by 2](./10-divisible_by_2.py) | Write a function that finds all multiples of 2 in a list. |
| [11. Delete at](./11-delete_at.py) | Write a function that deletes the item at a specific position in a list. |
| [12. Switch](./12-switch.py) | Complete the source code in order to switch value of a and b |
| [13. Linked list palindrome ](./13-is_palindrome.c) | Write a function in C that checks if a singly linked list is a palindrome. |
| [14. CPython #0: Python lists](./100-print_python_list_info.c) | Create a C function that prints some basic info about Python lists. |

## Author

* [GitHub - Luis Miguel Vargas](https://github.com/luismvargasg)

* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)