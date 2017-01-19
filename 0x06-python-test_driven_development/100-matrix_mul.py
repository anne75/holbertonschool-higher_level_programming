#!/usr/bin/python3
"""
This is the module 100-matrix_mul

This module contains only one function, matrix_mul
A test suite has been created for this module in ./tests
You can run it with python3 -m doctest -v ./tests/100-matrix_mul.txt
"""


def check_args(matrix, name):
    """
    Raises errors if matrix is not a matrix of numbers

    Arguments:
        matrix: should be a matrix (n * m) of numbers
        name: the variable name as a string

    Return: True maybe
    """
    allowed = (float, int)

    if not isinstance(matrix, list):
        raise TypeError("{} must be a list".format(name))

    rows_length = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("{} must be a list".format(name))
        rows_length.append(len(row))
        for element in row:
            if not isinstance(element, allowed) or type(element) is bool:
                raise TypeError("{} should contain only integers or floats"
                                .format(name))

# could use all(isinstance(x, allowed) for x in row)
    if len(rows_length) == 0 or max(rows_length) == 0:
        raise ValueError("{} can't be empty".format(name))

    if max(rows_length) != min(rows_length):
        raise TypeError("each row of {} must should be of the same size"
                        .format(name))

    return True


def matrix_mul(m_a, m_b):
    """
    Computes the product of 2 matrixes

    Arguments:
        m_a: a matrix of numbers
        m_b: a matrix of numbers

    Returns:
       the product of the matrixes
    """
    check_args(m_a, "m_a")
    check_args(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new = [[sum(m_a[j][i] * m_b[i][k] for i in range(len(m_b)))
            for k in range(len(m_b[0]))] for j in range(len(m_a))]
    return (new)
