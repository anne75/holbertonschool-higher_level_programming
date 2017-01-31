#!/usr/bin/python3
"""
This is module 101-add_attribute

This module contains on function
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an object
    """
    if ('__dict__' in dir(obj)):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
