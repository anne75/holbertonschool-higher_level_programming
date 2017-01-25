#!/usr/bin/python3
"""
This is module 3-rectangle

This module contains 1 class Rectangle
"""


class Rectangle:
    """
    defines class Rectangle

    **Instance attributes**
    width: private must be a non negative int
    height: private must be a non negative int

    **Instance methods**
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    __init__(self, width=0, height=0)
    __check_arg(self, value)
    area(self)
    perimeter(self)
    __str__(self)
    """

    def __init__(self, width=0, height=0):
        """
        Instantiates a Rectangle.

        Arguments:
            width: facultative, a non-negative int
            height: facultative, a non-negative int
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Getter of Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for Rectangle height

        Argument:
            value: non-negative int
        """
        if self.__check_arg(value, "height"):
            self.__height = value

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for Rectangle width

        Arguments:
            value: non negative int
        """
        if self.__check_arg(value, "width"):
            self.__width = value

    def __check_arg(self, value, attribute):
        """
        Checks the validity of the value to pass as instance attribute
        private

        Arguments:
            value
            attribute: name of the tentative attribute

        Returns:
            True or raise exception
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attribute))
        return (True)

    def area(self):
        """ Area of Rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ Perimeter of Rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """String representation of Rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        return ("\n".join(["#" * self.__width for i in range(self.__height)]))
