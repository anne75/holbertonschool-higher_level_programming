#!/usr/bin/python3
"""
This is module 1-square

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

    def __init__(self, size):
        """
        instantiate a Square object

        Arguments:
            size: whatever
        """
        self.__size = size
