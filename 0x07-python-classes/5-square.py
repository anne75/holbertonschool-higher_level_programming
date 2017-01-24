#!/usr/bin/python3
"""
This is module 5-square

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
    size(self)
    size(self, value)
    my_print(self)

    :Example:
    x = Square(3)
    x.size = 5
    x.area()
    x.my_print()
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

    def my_print(self):
        """
        prints the square in ascii art

        no arguments
        """
        print("\n".join(["#" * self.__size for i in range(self.__size)]))
