#!/usr/bin/python3
"""
This is module 3-kind_of_class

This module only contains one function
"""


def is_kind_of_class(obj, a_class):
    """
    evaluates if an object is of type a_class or a subclass of it

    Arguments:
        obj: an object
        a_class: a class

    Return:
        True if the object is of type class or a subclass of it,
        False otherwise
    """
    return isinstance(obj, a_class)
