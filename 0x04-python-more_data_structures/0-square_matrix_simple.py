#!/usr/bin/python3


def square_matrix(matrix=[]):
    """
    computes the square value of all elements in matrix

    matrix: a 1 or 2D array of ints

    Return: a new matrix
    """
    new = []
    try:
        new = [[x ** 2 for x in row] for row in matrix]
    except TypeError:
        new = [x ** 2 for x in matrix]
    return (new)
