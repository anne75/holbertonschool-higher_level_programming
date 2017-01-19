#!/usr/bin/python3
"""
This is module 4-print_square

This module only contains one function print_square

A test suite has been developed for this module in the /tests directory.
You can run it with
print_square = __import__('4-print_square').print_square
"""

def print_square(size):
    """
    prints a square of the desired size

    Arguments:
        size: must be a positive or 0 integer, size of square
    """
    if not isinstance(size, int) and not size is bool:
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")

    print("\n".join(["#" * size for j in range(size)]))
