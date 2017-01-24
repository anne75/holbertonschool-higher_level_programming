#!/usr/bin/python3
"""
This is module 101-square

This module contains one class Square
"""


class Square:
    """
    This class Square creates a square from a size

    **parameters**
    size: needed for instantiation, hidden (should it be mentioned here ?)
    position: tuple of 2 ints, hidden

    **functions**
    __init__(self, size)
    area(self)
    size(self)
    size(self, value)
    my_print(self)
    position(self)
    position(self, value)
    __str__(self)

    :Example:
    x = Square(3)
    x.size = 5
    x.area()
    x.my_print()
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        instantiate a Square object

        Arguments:
            size: must be a positive or null integer
        """
        self.size = size
        self.position = position

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
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        getter for the position attribute

        No arguments

        Return:
            the position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for the position attribute

        Arguments
            value: tuple of non negative int to be set to position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        computes the area of a square of a given size

        No arguments

        Return:
            area of square (int)
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        prints the square in ascii art

        no arguments
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.position[0] + "#" * self.__size
                             for i in range(self.__size)]))

    def __str__(self):
        """
        string format for print
        """
        if self.__size == 0:
            return ""
        string = "\n" * self.__position[1]
        string += "\n".join([" " * self.position[0] + "#" * self.__size
                             for i in range(self.__size)])
        return string
