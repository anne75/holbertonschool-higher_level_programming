#!/usr/bin/python3
"""
This is module 7-base_geometry

This module creates one class
A test suite has been created for this module. Runit with
python3 -m doctest ./tests/7-base_geometry.txt
"""


class BaseGeometry:
    """
    Class Base Geometry

    **public methods**
    area
    integer_validation
    """

    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the choice of value for name

        Arguments
            name: a name (string)
            value: should be a positive integer
        """
        if type(name) is not str:
            return
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
