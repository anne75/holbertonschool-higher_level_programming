#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    print a matrix of integers in pre-defined format
    """
    rows_list = []
    for row in matrix:
        if row:
            rows_list.append(" ".join(["{:d}".format(x) for x in row]))
    print("\n".join(rows_list))
