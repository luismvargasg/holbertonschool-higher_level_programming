# 0x05. Python - Exceptions

> This directory contains all the tasks of the project "0x05. Python - Exceptions" at [Holberton School](https://www.holbertonschool.com "Holberton School.") for educational purpose.

## General Objectives

* Whats the difference between errors and exceptions.
* What are exceptions and how to use them.
* When do we need to use exceptions.
* How to correctly handle an exception.
* Whats the purpose of catching exceptions.
* How to raise a builtin exception.
* When do we need to implement a clean-up action after an exception.

## Basic info

Until now error messages havent been more than mentioned, but if you have tried out the examples you have probably seen some. There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

### Syntax Errors
Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:
```
>>> while True print('Hello world')
  File "<stdin>", line 1, in ?
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

### Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here:
```
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: Can't convert 'int' object to str implicitly
```
For more information pleas visit: [Python Errors](https://docs.python.org/3.4/tutorial/errors.html)

## Directory Files

| **File** | **Description** |
|----------|-----------------|
| [0. Safe list printing](./0-square_matrix_simple.py) | Write a function that prints x elements of a list. |
| [1. Safe printing of an integers list](./1-safe_print_integer.py | Write a function that prints an integer with "{:d}".format(). |
| [2. Print and count integers](./2-safe_print_list_integers.py) | Write a function that prints the first x elements of a list and only integers. |
| [3. Integers division with debug](./3-safe_print_division.py) | Write a function that divides 2 integers and prints the result. |
| [4. Divide a list](./4-list_division.py) | Write a function that divides element by element 2 lists. |
| [5. Raise exception](5-raise_exception.py) | Write a function that raises a type exception. |
| [6. Raise a message](./6-raise_exception_msg.py) | Write a function that raises a name exception with a message. |
| [7. Safe integer print with error message](./100-safe_print_integer_err.py) | Write a function that prints an integer. |
| [8. Safe function](./101-safe_function.py) | Write a function that executes a function safely.  |
| [9. ByteCode -> Python #4](./102-magic_calculation.py) | Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode: |
| [10. CPython #2: PyFloatObject](./103-python.c) | Create three C functions that print some basic info about Python lists, Python bytes an Python float objects. |

## Author

* [GitHub - Luis Miguel Vargas](https://github.com/luismvargasg)

* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)
