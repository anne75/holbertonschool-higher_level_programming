#!/usr/bin/python3
import math
""" module comment"""


class MagicClass:
    """class Magic"""
    def __init__(self, radius=0):
        """instantiate"""
        self.__radius = 0
        if (type(radius) is not int) and (type(radius) is not float):
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """circle area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """circle perimeter"""
        return (2 * math.pi * self.__radius)

# see http://stackoverflow.com/a/19560286 for bytecode
