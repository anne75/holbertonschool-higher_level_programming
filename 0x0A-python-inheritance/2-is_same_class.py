#!/usr/bin/python3
"""
This is module 2-is_same_class

This module only defines one funtion
"""


def is_same_class(obj, a_class):
    """
    Evaluates if an object belongs to this class exactly

    Arguments:
        obj: an object
        a_class: a class

    Return:
        True if the object type matches the class exactly, Flase otherwise
    """
    return type(obj) == a_class
