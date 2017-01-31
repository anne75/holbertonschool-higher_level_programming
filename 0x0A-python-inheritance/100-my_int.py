#!/usr/bin/python3
"""
This is module 100-my_int

This module contains a rebal class
"""


class MyInt(int):
    """
    MyInt is a rebel
    subclass of int

    int with == and != inverted

    **static method**
    __new__ since int are immutable, needed to create a MyInt

    **instance methods**
    __ne__
    __eq__
    """

    def __new__(cls, value):
        """ creates a new object """
        return super().__new__(cls, value)


    def __eq__(self, other):
        """ inverts the meaning """
        if super().__eq__(other):
            return False
        return True

    def __ne__(self, other):
        """ inverts the meaning """
        if self.__eq__(other):
            return False
        return True
