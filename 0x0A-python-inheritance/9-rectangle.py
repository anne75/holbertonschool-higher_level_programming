#!/usr/bin/python3
"""
This is module 9-rectangle

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

    **methods**
    area
    __str__
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

    def area(self):
        """computes area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns nice string"""
        return "[Rectangle] {width}/{height}".format(width=self.__width,
                                                     height=self.__height)
