#!/usr/bin/python3
"""
This is the 0-add_integer module.

This module supplies one function: add_integer

To test this module, a text file is provided in the /tests directory
You could run python3 -m doctest -v ./tests/0-add_integer.txt
"""


def add_integer(a, b):
    """
    Does the addition of two integers

    Arguments:
        a: should be an integer, if a float it will be cast to integer
        b: should be an integer, if a float it will be cast to integer

    Return:
        a + b or raise error if input not a number
    """
    allowed = (float, int)
    if not isinstance(a, allowed) or type(a) is bool:
        raise TypeError("a must be an integer")
    if not isinstance(b, allowed) or type(b) is bool:
        raise TypeError("b must be an integer")

    a_int = int(a)
    b_int = int(b)
    return(a_int + b_int)
