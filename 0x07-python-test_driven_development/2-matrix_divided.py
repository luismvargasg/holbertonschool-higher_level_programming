#!/usr/bin/python3
"""matrix elements division

Usage example:
print(matrix_divided([[1, 2, 3], [4, 5, 6]], 3))
"""


def matrix_divided(matrix, div):
    """function that adds 2 divides all elements of a matrix.

    Args:
        matrix: must be a list of integers or floats.
        div: must be a number (integer or float).

    Returns:
         a new matrix: with the result of the division of each elem.

    Raises:
        TypeError: if matrix is not a list of list of integers or floats.
        TypeError: if the len of each row is not the same.
        ZeroDivisionError: div cant be equal to 0.
    """
    i = 0
    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of" +
                        " integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of" +
                            " integers/floats")
        for item in row:
            if type(item) not in [int, float] or item != item:
                raise TypeError("matrix must be a matrix (list of lists) of" +
                                " integers/floats")
    for i in range(0, (len(matrix) - 1)):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [[round(items / div, 2) for items in rows] for rows in matrix]
    return new_matrix
