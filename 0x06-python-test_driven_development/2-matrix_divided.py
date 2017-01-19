#!/usr/bin/python3
"""
This is the 2-matrix_divided module

The module supplies only one function to divide a matrix by a number
A doctest has been created for this module in the /tests directory
It can be run with
python3 -m doctest -v ./tests/2-matrix_divided.txt

"""


def matrix_divided(matrix, div):
    """
    Divides a matrix by a number

    Arguments:
        matrix: must be an array of arrays of floats or ints of the same size
        div: the divisor, must be a non 0 number

    Returns:
        a matrix were all values have been divided, rounded to 2 decimal places
    """
    allowed = (float, int)
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, allowed):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(error)

    rows_length = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error)
        rows_length.append(len(row))
        for element in row:
            if not isinstance(element, allowed):
                raise TypeError(error)

# could use all(isinstance(x, allowed) for x in row)
    if not rows_length or len(rows_length) == 0:
        raise TypeError(error)

    if max(rows_length) != min(rows_length) or max(rows_length) == 0:
        raise TypeError(error)

    new = [[round(n / div, 2) for n in row] for row in matrix]
    return (new)
