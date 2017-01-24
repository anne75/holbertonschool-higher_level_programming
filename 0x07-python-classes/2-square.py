#!/usr/bin/python3
"""
This is module 2-square

This module contains one class Square
"""


class Square:
    """
    This class Square does not do anything

    **parameters**
    size: needed for instantiation, hidden (should it be mentioned here ?)

    **functions**
    __init__(self, size)

    :Example:
    x = Square(3)
    """

    def __init__(self, size=0):
        """
        instantiate a Square object

        Arguments:
            size: must be a positive or null integer
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

# I am not use decorators as the attribute is private (no getter)
# actually it throws an error if I only use setter
