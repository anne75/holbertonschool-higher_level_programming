#!/usr/bin/python3
"""
This is module 3-square

This module contains one class Square
"""


class Square:
    """
    This class Square creates a square from a size

    **parameters**
    size: needed for instantiation, hidden (should it be mentioned here ?)

    **functions**
    __init__(self, size)
    area(self)

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

    def area(self):
        """
        computes the area of a square of a given size

        No arguments

        Return:
            area of square (int)
        """
        return (self.__size * self.__size)
