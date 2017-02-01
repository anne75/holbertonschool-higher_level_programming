#!/usr/bin/python3
"""
This is module 11-square

This module contains one class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Creates a Square
    Subclass from Rectangle

    **Instance attribute**
    size: an int >= 0

    **methods**
    __init__
    __str__
    """
    def __init__(self, size):
        """
        Instantiates a square

        Arguments:
        size: must be an int >= 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """makes nice string"""
        return "[{}] {size}/{size}".format(self.__class__.__name__,
                                           size=self.__size)
