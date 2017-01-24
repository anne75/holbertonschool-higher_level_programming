#!/usr/bin/python3
"""
This is module 4-square

This module contains one class Square

A test suite has been built for this module in the tests folder
It can be run with
python3 -m doctest -v /tests/4-square.txt
"""


class Square:
    """
    This class Square creates a square from a size

    **parameters**
    size: needed for instantiation, hidden (should it be mentioned here ?)

    **functions**
    __init__(self, size)
    area(self)
    size(self)
    size(self, value)

    :Example:
    x = Square(3)
    """

    def __init__(self, size=0):
        """
        instantiate a Square object

        Arguments:
            size: must be a positive or null integer
        """
        self.size = size

    def area(self):
        """
        computes the area of a square of a given size

        No arguments

        Return:
            area of square (int)
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        getter for the size attribute

        No arguments

        Return:
            the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for the size attribute

        Arguments
            value: value to be passed to size, should be an int >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


# getters and underscores http://stackoverflow.com/a/28464787
