#!/usr/bin/python3
"""
This is module 8-rectangle

This module contains one class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    subclass of BaseGeometry

    **instance attributes**
    width: private
    height: private
    """

    def __init__(self, width, height):
        """
        instantiates a Rectangle is wodth and height are positive int

        Arguments:
            width: must be positive int
            height: must be positive int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
